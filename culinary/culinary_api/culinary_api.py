import requests
from culinary.variables import ENV_VARS

API_KEY = ENV_VARS['API_KEY']


def search_recipies_by_ingredients(query, number=5):
    url = f'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'apiKey': API_KEY,
        'ingredients': query,
        'number': number,
        'limitLicense': True,
        'ranking': 1,
        'ignorePantry': False,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return []


def search_recipe(query, number=5):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': number,
        'instructionRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
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
        'includeNutrition': False,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        recipe_details = {
            "title": data.get("title"),
            "ready_in_minutes": data.get("readyInMinutes"),
            "number_of_ingredients": len(data.get("extendedIngredients", [])),
            "ingredients": list({
                (ing["name"], ing["original"], ing["amount"], ing["unit"])
                for ing in data.get("extendedIngredients", [])
            }),
            "image": data.get("image"),
            "dish_type": data.get("dishTypes"),
        }
        recipe_details['ingredients'] = [
            {
                "name": name,
                "original": original,
                "amount": amount,
                "unit": unit,
            }
            for name, original, amount, unit in recipe_details['ingredients']
        ]
        return recipe_details
    except Exception as e:
        print(f'Error {e}')
        return None
