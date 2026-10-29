from app.auth import create_token
from app.routes import app


def test_me_role_returns_only_role_for_authenticated_user() -> None:
    """Return just the logged-in user's role."""
    client = app.test_client()
    token = create_token("asha")

    response = client.get(
        "/me/role",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.get_json() == {"role": "admin"}


def test_me_role_rejects_unauthenticated_request() -> None:
    """Reject requests without an authentication token."""
    client = app.test_client()

    response = client.get("/me/role")

    assert response.status_code == 401
    assert response.get_json() == {"error": "unauthorized"}


def test_me_role_returns_not_found_for_unknown_user() -> None:
    """Return a formatted error if an authenticated user record is missing."""
    client = app.test_client()
    token = create_token("unknown-user")

    response = client.get(
        "/me/role",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 404
    assert response.get_json() == {"error": "user not found"}
