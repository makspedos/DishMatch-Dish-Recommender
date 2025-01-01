import pytest

from culinary.culinary_api import culinary_api


def test_form_find(client):
    response = client.get('/?search-value=Hi')
    assert response.status_code == 200
    assert response.request.args['search-value'] == 'Hi'
    #assert b'Hi' in response.data        #if we want to check existence of the word in tempalte


def test_empty_form(client):
    response = client.get('/?search-value=')
    assert response.status_code == 200
    assert response.request.args['search-value'] != 'Hi'


@pytest.mark.parametrize('query, number, expected', [
    ('Chicken soup', 2, 'soup'),
    ('5555', 0, [])
])
def test_search_recipes(query, number, expected):
    search_result = culinary_api.search_recipe(query=query, number=2)
    assert len(search_result) == number
    if len(search_result) > 0:
        assert expected in str.lower(search_result[0]['title'])
    else:
        assert expected == search_result


# @pytest.mark.parametrize('id, expected', [(555, 'ingredients'), (9999999, None)])
# def test_get_recipy_by_id(id, expected):
#     searched_dish = culinary_api.get_recipe_by_id(id)
#     if len(searched_dish)>0:
#         assert expected in searched_dish
#     else:
#         assert searched_dish == expected
