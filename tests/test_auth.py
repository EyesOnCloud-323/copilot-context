from app.auth import create_token, decode_token

def test_token_round_trip():
    token = create_token("asha")
    assert decode_token(token) == "asha"

def test_bad_token_returns_none():
    assert decode_token("not-a-token") is None
