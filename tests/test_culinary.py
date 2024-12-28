def test_form_find(client):
    response = client.get('/?search-value=Hi')
    assert response.status_code == 200
    assert response.request.args['search-value']=='Hi'
    #assert b'Hi' in response.data        #if we want to check existence of the word in tempalte

def test_empty_form(client):
    response = client.get('/?search-value=')
    assert response.status_code ==200
    assert response.request.args['search-value']!='Hi'
