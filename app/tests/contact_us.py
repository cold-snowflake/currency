def test_get_contact_us_list(client):
    response = client.get('/currency/contact/create/')
    assert response.status_code == 200


def test_post_contact_us_empety_form_200(client):
    response = client.post('/currency/contact/create/')
    assert response.status_code == 200


def test_post_contact_us_empety_form_errors(client):
    response = client.post('/currency/contact/create/')
    assert response.context_data['form'].errors == {
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
        }


def test_post_contact_us_invalid_reply_to_200(client):
    payload = {
        'email_from': 'INVALID EMAIL',
        'subject': 'SUBJECT',
        'message': 'MESSAGE'
        }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.status_code == 200


def test_post_contact_us_invalid_reply_to_errors(client):
    payload = {
        'email_from': 'INVALID EMAIL',
        'subject': 'SUBJECT',
        'message': 'MESSAGE'
        }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.context_data['form'].errors == {
        'email_from': ['Enter a valid email address.']
        }


def test_post_contact_us_valid_data_302(client):
    payload = {
        'email_from': 'example@gmail.com',
        'subject': 'SUBJECT',
        'message': 'MESSAGE'
    }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.status_code == 302


def test_post_contact_us_valid_data_location(client):
    payload = {
        'email_from': 'example@gmail.com',
        'subject': 'SUBJECT',
        'message': 'MESSAGE'
    }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.headers['Location'] == '/currency/contact/list/'
