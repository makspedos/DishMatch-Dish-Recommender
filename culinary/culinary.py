import json
from flask import Blueprint, render_template, request, session
from .culinary_api.culinary_api import *
from database import DatabaseManipulator
from uuid import uuid4
from .recommendation import AssociationRecommender
from .mock_data import get_mock_dishes, get_mock_ingredients

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')
db = DatabaseManipulator()


@culinary_bp.route('/', methods=['GET', 'POST'])
def form_find():
    value = request.args.get('search-value')
    #recipes = get_mock_dishes() # Use this line if you want to use mock dishes
    recipes = search_recipe(value)
    session_id = session.get('session_id', str(uuid4()))
    session['session_id'] = session_id

    user = db.find_user(session_id)

    if request.method == 'POST':
        if 'ingredients_dish' in request.form:
            try:
                dish_ingredients = json.loads(request.form['ingredients_dish'].replace("'", '"'))
                #dish_ingredients = get_mock_ingredients() # Use this line if you want to use mock ingredients
                user_dish = {
                    'ingredients': [item['name'] for item in dish_ingredients[:8]],
                }
                updated_user = db.create_or_update_user(session_id=session_id, user_data=user_dish)

                recommender = AssociationRecommender()
                # Retrieve user preferences from database
                if updated_user:
                    recommended_products = recommender.get_user_preferences(updated_user)
                    db.create_or_update_user(session_id=session_id, recommended_products=recommended_products)
                    print(recommended_products)
            except Exception as e:
                print(request.form['ingredients_dish'])
                print(f"Error: {e}")

    return render_template('html/index.html',
                           value=value,
                           recipes=recipes)


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
