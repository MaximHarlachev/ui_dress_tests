import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData

# import logging

from pages.application import Application

# logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    # logger.info(f'Start browser, url is {base_url}')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install(),
                                           chrome_options=chrome_options), base_url)
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    data = AuthData(login=user, password=password)
    app.login.auth(data)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="max",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Fak2@oprE",
        help="enter password",
    )
