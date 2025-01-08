import requests
from culinary.variables import ENV_VARS

API_KEY = ENV_VARS['API_KEY']

def search_recipies_by_ingredients(query,number=10):
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
        response = requests.get(url, params = params)
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

def get_mock_result():
    list_of_dishes = [
        {"title": "Жарена картопля", "image": ""},
        {"title": "Фарш з макаронами", "image": ""},
        {"title": "Гречка", "image": ""},
        {"title": "Борщ", "image": ""},
        {"title": "Пельмені", "image": ""},
        {"title": "Вареники з картоплею", "image": ""},
        {"title": "Млинці", "image": ""},
        {"title": "Омлет", "image": ""},
        {"title": "Паста Карбонара", "image": ""},
        {"title": "Курячий суп", "image": ""},
        {"title": "Салат Олів'є", "image": ""},
        {"title": "Котлети", "image": ""},
        {"title": "Суп Харчо", "image": ""},
        {"title": "Голубці", "image": ""},
        {"title": "Рагу з овочів", "image": ""},
        {"title": "Піца Маргарита", "image": ""},
        {"title": "Шаурма", "image": ""},
        {"title": "Баклажани по-корейськи", "image": ""},
        {"title": "Плов", "image": ""},
        {"title": "Тушкована капуста", "image": ""},
        {"title": "Запіканка сирна", "image": ""},
        {"title": "Курка-гриль", "image": ""},
        {"title": "Бургер", "image": ""},
        {"title": "Риба на пару", "image": ""},
        {"title": "Шашлик", "image": ""},
        {"title": "Уха", "image": ""},
        {"title": "Тефтелі", "image": ""},
        {"title": "Лазанья", "image": ""},
        {"title": "Біфстроганов", "image": ""},
        {"title": "Том Ям", "image": ""},
        {"title": "Цезар", "image": ""},
        {"title": "Картопля фрі", "image": ""},
        {"title": "Панкейки", "image": ""},
        {"title": "Сирники", "image": ""},
        {"title": "Фалафель", "image": ""},
        {"title": "Рататуй", "image": ""},
        {"title": "Ролли Філадельфія", "image": ""},
        {"title": "Бісквітний торт", "image": ""},
        {"title": "Лобіо", "image": ""},
        {"title": "Салат з крабовими паличками", "image": ""},
        {"title": "Картопляне пюре", "image": ""},
        {"title": "Солянка", "image": ""},
        {"title": "Хачапурі", "image": ""},
        {"title": "Суп з фрикадельками", "image": ""},
        {"title": "Томатний суп", "image": ""},
        {"title": "Капучино", "image": ""},
        {"title": "Кекс з родзинками", "image": ""},
        {"title": "Буріто", "image": ""},
        {"title": "Тірамісу", "image": ""},
        {"title": "Чахохбілі", "image": ""}
    ]

    return list_of_dishes