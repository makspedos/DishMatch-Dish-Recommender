import random
from culinary.culinary_api.culinary_api import search_recipies_by_ingredients


def examine_dishes(user_id, db):
    user = db.find_user(user_id)
    recommended_dishes = None
    if user:
        recommended_ingredients = user['recommended_ingredients']
        if recommended_ingredients:
            recommended_dishes = search_recipies_by_ingredients(recommended_ingredients, number=3)
            #recommended_dishes = get_mock_dishes()[:3]
            print(recommended_dishes)
    return recommended_dishes


def get_mock_dishes():
    list_of_dishes = [
        {"recipe_id": 1, "title": "Жарена картопля", "image": ""},
        {"recipe_id": 2, "title": "Фарш з макаронами", "image": ""},
        {"recipe_id": 3, "title": "Гречка", "image": ""},
        {"recipe_id": 4, "title": "Борщ", "image": ""},
        {"recipe_id": 5, "title": "Пельмені", "image": ""},
        {"recipe_id": 6, "title": "Вареники з картоплею", "image": ""},
        {"recipe_id": 7, "title": "Млинці", "image": ""},
        {"recipe_id": 8, "title": "Омлет", "image": ""},
        {"recipe_id": 9, "title": "Паста Карбонара", "image": ""},
        {"recipe_id": 10, "title": "Курячий суп", "image": ""},
        {"recipe_id": 11, "title": "Салат Олів'є", "image": ""},
        {"recipe_id": 12, "title": "Котлети", "image": ""},
        {"recipe_id": 13, "title": "Суп Харчо", "image": ""},
        {"recipe_id": 14, "title": "Голубці", "image": ""},
        {"recipe_id": 15, "title": "Рагу з овочів", "image": ""},
        {"recipe_id": 16, "title": "Піца Маргарита", "image": ""},
        {"recipe_id": 17, "title": "Шаурма", "image": ""},
        {"recipe_id": 18, "title": "Баклажани по-корейськи", "image": ""},
        {"recipe_id": 19, "title": "Плов", "image": ""},
        {"recipe_id": 20, "title": "Тушкована капуста", "image": ""},
        {"recipe_id": 21, "title": "Запіканка сирна", "image": ""},
        {"recipe_id": 22, "title": "Курка-гриль", "image": ""},
        {"recipe_id": 23, "title": "Бургер", "image": ""},
        {"recipe_id": 24, "title": "Риба на пару", "image": ""},
        {"recipe_id": 25, "title": "Шашлик", "image": ""},
        {"recipe_id": 26, "title": "Уха", "image": ""},
        {"recipe_id": 27, "title": "Тефтелі", "image": ""},
        {"recipe_id": 28, "title": "Лазанья", "image": ""},
        {"recipe_id": 29, "title": "Біфстроганов", "image": ""},
        {"recipe_id": 30, "title": "Том Ям", "image": ""},
        {"recipe_id": 31, "title": "Цезар", "image": ""},
        {"recipe_id": 32, "title": "Картопля фрі", "image": ""},
        {"recipe_id": 33, "title": "Панкейки", "image": ""},
        {"recipe_id": 34, "title": "Сирники", "image": ""},
        {"recipe_id": 35, "title": "Фалафель", "image": ""},
        {"recipe_id": 36, "title": "Рататуй", "image": ""},
        {"recipe_id": 37, "title": "Ролли Філадельфія", "image": ""},
        {"recipe_id": 38, "title": "Бісквітний торт", "image": ""},
        {"recipe_id": 39, "title": "Лобіо", "image": ""},
        {"recipe_id": 40, "title": "Салат з крабовими паличками", "image": ""},
        {"recipe_id": 41, "title": "Картопляне пюре", "image": ""},
        {"recipe_id": 42, "title": "Солянка", "image": ""},
        {"recipe_id": 43, "title": "Хачапурі", "image": ""},
        {"recipe_id": 44, "title": "Суп з фрикадельками", "image": ""},
    ]

    return list_of_dishes


def get_mock_ingredients():
    mock_ingredients = [
        {"name": "Tomato", "original": "2 medium tomatoes", "amount": 2, "unit": "tomatoes"},
        {"name": "Onion", "original": "1 large onion", "amount": 1, "unit": "onion"},
        {"name": "Garlic", "original": "3 cloves of garlic", "amount": 3, "unit": "cloves"},
        {"name": "Carrot", "original": "1 large carrot", "amount": 1, "unit": "carrot"},
        {"name": "Potato", "original": "2 large potatoes", "amount": 2, "unit": "potatoes"},
    ]
    mock_ingredients2 = [
        {"name": "Chicken", "original": "1 pound boneless chicken breast", "amount": 1, "unit": "pound"},
        {"name": "Rice", "original": "2 cups cooked white rice", "amount": 2, "unit": "cups"},
        {"name": "Peas", "original": "1 cup frozen peas", "amount": 1, "unit": "cup"},
        {"name": "Carrot", "original": "2 medium carrots", "amount": 2, "unit": "carrots"},
        {"name": "Onion", "original": "1 medium onion", "amount": 1, "unit": "onion"},
    ]
    mock_ingredients3 = [
        {"name": "Beef", "original": "1 pound ground beef", "amount": 1, "unit": "pound"},
        {"name": "Lettuce", "original": "2 cups shredded lettuce", "amount": 2, "unit": "cups"},
        {"name": "Tomato", "original": "1 large tomato", "amount": 1, "unit": "tomato"},
        {"name": "Cheese", "original": "1 cup shredded cheddar cheese", "amount": 1, "unit": "cup"},
        {"name": "Bread", "original": "4 slices of whole wheat bread", "amount": 4, "unit": "slices"},
    ]
    returned_list = random.choice([mock_ingredients, mock_ingredients2, mock_ingredients3])
    return returned_list