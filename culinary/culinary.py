import requests
from flask import Blueprint, render_template, request
from variables import ENV_VARS
culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')

API_KEY = ENV_VARS['API_KEY']

@culinary_bp.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    recipes = search_recipe(value)
    return render_template('html/index.html', value=value, recipes=recipes)


def search_recipe(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 3,
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
