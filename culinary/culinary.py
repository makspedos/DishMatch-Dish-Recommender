import requests
from flask import Blueprint, render_template, request
from .variables import ENV_VARS

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')

API_KEY = ENV_VARS['API_KEY']

@culinary_bp.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    recipes = search_recipe(value)
    print(recipes)
    return render_template('html/index.html', value=value, recipes=recipes)


@culinary_bp.route('/<string:dish_id>/', methods=['GET'])
def dish_page(dish_id):
    dish = get_recipe_by_id(dish_id)
    ingredients = ''
    if dish:
        ingredients = dish['extendedIngredients']
    else:
        dish = 'Not found'
    return render_template('html/dish.html', dish=dish, ingredients=ingredients)


def search_recipe(query, number=3):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': number,
        'instructionRequired':True,
        'addRecipeInformation': True,
        'fillIngredients':True,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    except Exception as e:
        print(f'Error {e}')
        return []

def get_recipe_by_id(id):
    url = f'https://api.spoonacular.com/recipes/{id}/information'
    params = {
        'apiKey': API_KEY,
        'includeNutrition':False,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        recipe_details = {
            "title": data.get("title"),
            "summary": data.get("summary"),
            "servings": data.get("servings"),
            "ready_in_minutes": data.get("readyInMinutes"),
            "number_of_ingredients": len(data.get("extendedIngredients", [])),
            "ingredients": [
                {"name": ing["name"], "amount": ing["amount"], "unit": ing["unit"]}
                for ing in data.get("extendedIngredients", [])
            ],
            "instructions": data.get("instructions"),
            "image": data.get("image"),
        }

        return recipe_details
    except Exception as e:
        print(f'Error {e}')
        return None