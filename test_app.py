from app import create_app


def test_home_page():
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/') # noqa
        assert response.status_code == 200 # noqa
        assert b"Welcome to the Flask User Management Example!" in response.data # noqa
        assert b"Need an account?" in response.data # noqa
        assert b"Existing user?" in response.data # noqa
