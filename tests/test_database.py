
def test_create_user_with_ingredients(db, user_id, user_data):
    result_user = db.create_or_update_user(session_id=user_id, user_data=user_data)
    faked_data = {'ingredients':['Жарена котлета', 'Фарш', 'Вареники']}
    assert result_user is not None
    assert len(result_user['user_dish'][0]) > 0
    assert result_user['user_dish'][0]['ingredients'] == user_data['ingredients']
    assert result_user['user_dish'][0]['ingredients'] != faked_data['ingredients']


def test_add_recommendation(db, user_id, recommended_ingredients):
    result_user = db.create_or_update_user(session_id=user_id, recommended_ingredients=recommended_ingredients)
    assert result_user['recommended_ingredients'] is not None
    assert len(result_user['recommended_ingredients']) == 3
    assert result_user['recommended_ingredients'] == recommended_ingredients


def test_not_found_user(db, user_id):
    user = db.find_user(user_id)
    print(user)
    assert user is None

def test_found_user(db, user_id, user_data):
    db.create_or_update_user(session_id=user_id, user_data=user_data)
    user = db.find_user(user_id)
    assert user is not None
    assert user['session_id'] == user_id