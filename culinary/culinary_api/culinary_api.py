import requests
from culinary.variables import ENV_VARS

API_KEY = ENV_VARS['API_KEY']


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
                {"name": ing["name"], "original": ing["original"], "amount": ing["amount"], "unit": ing["unit"]}
                for ing in data.get("extendedIngredients", [])
            ],
            "image": data.get("image"),
        }
        return recipe_details
    except Exception as e:
        print(f'Error {e}')
        return None