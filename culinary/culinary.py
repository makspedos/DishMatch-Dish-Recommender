from flask import Blueprint, render_template, request
from .culinary_api.culinary_api import *

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')


@culinary_bp.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    recipes = search_recipe(value)
    print(recipes)
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


