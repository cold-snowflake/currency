from currency.models import Source


def test_get_api_rates(api_client_auth):
    response = api_client_auth.get('/api/currency/rates/')
    assert response.status_code == 200


def test_get_api_rates_json(api_client_auth):
    response = api_client_auth.get('/api/currency/rates/')
    assert response.json()


def test_post_api_rates(api_client_auth):
    response = api_client_auth.post('/api/currency/rates/')
    assert response.status_code == 400


def test_post_api_rates_empty(api_client_auth):
    response = api_client_auth.post('/api/currency/rates/')
    assert response.json() == {
        'buy': ['This field is required.'],
        'sell': ['This field is required.'],
        'source': ['This field is required.']
        }


def test_post_api_rates_valid(api_client_auth):
    source = Source.objects.create(name='test', code_name='test')
    payload = {
        'buy': '31.23',
        'sell': '35.55',
        'source': source.id,
        }
    response = api_client_auth.post('/api/currency/rates/', data=payload)
    assert response.status_code == 201


def test_get_api_source(api_client_auth):
    response = api_client_auth.get('/api/currency/sources/')
    assert response.status_code == 200


def test_get_api_source_json(api_client_auth):
    response = api_client_auth.get('/api/currency/sources/')
    assert response.json()


def test_post_api_sources(api_client_auth):
    response = api_client_auth.post('/api/currency/sources/')
    assert response.status_code == 400


def test_post_api_sources_empty(api_client_auth):
    response = api_client_auth.post('/api/currency/sources/')
    assert response.json() == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.']
        }


def test_post_api_sources_valid(api_client_auth):
    payload = {
        'source_url': 2,
        'name': 'Name'
        }
    response = api_client_auth.post('/api/currency/sources/', data=payload)
    assert response.status_code == 201


def test_post_api_sources_invalid(api_client_auth):
    payload = {
        'source_url': 2,
        'name': 'Name' * 50
        }
    response = api_client_auth.post('/api/currency/sources/', data=payload)
    assert response.status_code == 400


def test_source_delete(api_client_auth):
    response = api_client_auth.delete("/api/currency/source/detail-delete/2/")
    assert response.status_code == 204
