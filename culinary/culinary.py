from flask import Blueprint, render_template, request
from .culinary_api.culinary_api import *
from .recommendation import RecommendAlgorithm

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')


@culinary_bp.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    #recipes = get_mock_result()
    recommended_recipes = []
    recipes = search_recipe(value)

    if value:
        recommended_title = RecommendAlgorithm()
        recipes_list = [recipe['title'] for recipe in recipes]
        result_dish_titles = recommended_title.recommend_by_title(value, recipes_list)
        print(result_dish_titles)
        for dish in recipes:
            if dish['title'] in result_dish_titles:
                recommended_recipes.append(dish)
        recipes= recipes[:5]

    return render_template('html/index.html', value=value, recipes=recipes, recommended_recipes=recommended_recipes)


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


