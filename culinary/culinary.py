import json
from flask import Blueprint, render_template, request, session
from .culinary_api.culinary_api import *
from database import DatabaseManipulator
from uuid import uuid4
from .recommendation import RecommendAlgorithm, get_user_preferences

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')
db = DatabaseManipulator()


@culinary_bp.route('/', methods=['GET', 'POST'])
def form_find():
    value = request.args.get('search-value')
    #recipes = get_mock_result() # Use this line if you want to use mock data
    recipes = search_recipe(value)
    user_session = db.find_user(session.get('session_id', 'anonymous'))

    if request.method == 'POST':
        if 'ingredients_dish' in request.form:
            ingredients_dish = json.loads(request.form['ingredients_dish'].replace("'", '"'))
            cooktime_dish = request.form.get('cooktime_dish')
            dish_type = request.form.get('dish_type')

            if 'session_id' not in session:
                session['session_id'] = str(uuid4())

            session_id = session.get('session_id', 'anonymous')

            user_dish = {
                'type': dish_type,
                'ingredients': [item['name'] for item in ingredients_dish],
                'cooktime_dish': cooktime_dish
            }
            db.create_or_update_user(session_id=session_id, user_data=user_dish)


    if user_session:
        # Retrieve user preferences from database
        recommended_products = get_user_preferences(user_session)
        return render_template('html/index.html',
                                value=value,
                                recipes=recipes,
                                recommended_products=recommended_products)
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
