from flask import Blueprint, render_template, request, session
from .culinary_api.culinary_api import *
from database import connect_db
from uuid import uuid4

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')
db = connect_db()

@culinary_bp.route('/', methods=['GET', 'POST'])
def form_find():
    value = request.args.get('search-value')
    #recipes = get_mock_result()
    recipes = search_recipe(value)

    if request.method == 'POST':
        interested_type = request.form.get('interested_dish')
        print(f'Type: {interested_type}')
        if 'session_id' not in session:
            session['session_id'] = str(uuid4())
        session_id = session.get('session_id', 'anonymous')

        db.user.update_one(
            {'session_id':session_id},
            {'$push':{'interested_dish':interested_type}},upsert=True)

    return render_template('html/index.html', value=value, recipes=recipes)


@culinary_bp.route('/<string:dish_id>/', methods=['GET'])
def dish_page(dish_id):
    previous_url = request.referrer
    dish = get_recipe_by_id(dish_id)
    ingredients = ''
    if dish:
        ingredients = dish['ingredients']
    else:
        dish = 'Not found'
    return render_template('html/dish.html', dish=dish, ingredients=ingredients, previous_url=previous_url)


