import json
from flask import Blueprint, render_template, request, session
from .culinary_api.culinary_api import *
from database import DatabaseManipulator
from uuid import uuid4
from .recommendation import AssociationRecommender
from .culinary_functions import examine_dishes

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')
db = DatabaseManipulator()


@culinary_bp.route('/', methods=['GET', 'POST'])
def form_find():
    value = request.args.get('search-value')
    recipes = search_recipe(value)
    session_id = session.get('session_id', str(uuid4()))
    session['session_id'] = session_id

    recommended_dishes = examine_dishes(user_id=session_id, db=db)

    if request.method == 'POST':
        if 'ingredients_dish' in request.form:
            try:
                dish_ingredients = json.loads(request.form['ingredients_dish'].replace("'", '"'))
                user_dish = {
                    'ingredients': [item['name'] for item in dish_ingredients[:8]],
                }
                updated_user = db.create_or_update_user(session_id=session_id, user_data=user_dish)

                recommender = AssociationRecommender()
                # Retrieve user preferences from database
                if updated_user:
                    recommended_ingredients = recommender.get_user_preferences(updated_user)
                    db.create_or_update_user(session_id=session_id, recommended_ingredients=recommended_ingredients)
                    print(recommended_ingredients)
            except Exception as e:
                print(request.form['ingredients_dish'])
                print(f"Error: {e}")

    return render_template('html/index.html',
                           value=value,
                           recipes=recipes, recommended_dishes=recommended_dishes)


@culinary_bp.route('/dish/<string:dish_id>/', methods=['GET'])
def dish_page(dish_id):
    previous_url = request.referrer
    dish = get_recipe_by_id(dish_id)
    ingredients = ''
    if dish:
        ingredients = dish['ingredients']
    else:
        dish = 'Not found'
    return render_template('html/dish.html',
                           dish=dish,
                           ingredients=ingredients,
                           previous_url=previous_url)
