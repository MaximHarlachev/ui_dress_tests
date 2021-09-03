import pytest

from models.auth import AuthData


class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="max", password="Fak2@oprE")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        app.personal_data.edit_personal_data()
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @pytest.mark.parametrize(
        "data",
        [
            {"name": "", "lastname": "", "email": ""},
            {"name": "", "lastname": "Харлачёв", "email": "negazirovannyi@inbox.ru"},
            {"name": "Максим", "lastname": "", "email": "negazirovannyi@inbox.ru"},
            {"name": "Максим", "lastname": "Харлачёв", "email": ""},
            {"name": "Максим", "lastname": "Харлачёв", "email": "negazirovannyiinbox.ru"},
            {"name": "Максим", "lastname": "Харлачёв", "email": "inbox.ru"},
        ],
    )
    def test_invalid_edit_basic_personal_data(self, app, data):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successfully
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="max", password="Fak2@oprE")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        app.personal_data.edit_personal_data(**data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"
