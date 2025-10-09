from utils.security.criptografy import Criptografy


def test_hash_password():
    criptografy = Criptografy()
    plain_text = "my_secret_password"
    hashed = criptografy.hash_password(plain_text)
    assert hashed != plain_text

def test_verify_password_when_incorrect():
    criptografy = Criptografy()
    plain_text = "my_secret_password"
    hashed = criptografy.hash_password(plain_text)
    assert criptografy.verify_password(plain_text, hashed)
    assert not criptografy.verify_password("wrong_password", hashed)

def test_verify_password_when_correct():
    criptografy = Criptografy()
    plain_text = "my_secret_password"
    hashed = criptografy.hash_password(plain_text)
    assert criptografy.verify_password(plain_text, hashed)