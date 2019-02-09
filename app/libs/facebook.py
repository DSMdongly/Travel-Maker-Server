import requests

FACEBOOK_OPENAPI_HOST = 'https://graph.facebook.com'


def get_user_data(token):
    resp = requests.get(FACEBOOK_OPENAPI_HOST + '/me', params={
        'access_token': token,
        'fields': 'id,name,email',
    })

    if resp.status_code != 200:
        return {}

    user_data = resp.json()

    return {
        'id': user_data.get('id'),
        'name': user_data.get('name'),
        'email': user_data.get('email'),
    }
