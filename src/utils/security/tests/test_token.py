from utils.security.token import Token

def test_generate_access_token():
    token = Token()
    data = {'sub': 'testuser'}
    access_token = token.create_access_token(data)
    assert access_token is not None

def test_decode_access_token():
    token = Token()
    data = {'sub': 'testuser'}
    access_token = token.create_access_token(data)
    decode_data = token.decode_access_token(access_token)
    assert decode_data['sub'] == 'testuser'