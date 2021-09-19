from selenium.webdriver.remote.webelement import WebElement

# from conftest import logger
from locators.base_page_locators import BasePageLocators
from locators.personal_data_page_locators import PersonalPageLocators
from models.auth import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def is_exit_confire_button(self):
        element = self.find_elements(LoginPageLocators.EXIT_CONFIRM)
        if len(element) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def exit_confire(self):
        return self.find_element(BasePageLocators.CONFIRM_EXIT_BUTTON)

    def auth(self, data: AuthData):
        # logger.info(f'Try to auth with login {data.login}, password {data.password}')
        # Проверка, есть ли кнопка подтверждения выхода
        if self.is_exit_confire_button():
            self.click_element(self.exit_confire()[0])
        # Проверка, авторизованы ли мы
        elif self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def user_menu_settings(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU_SETTINGS)

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(PersonalPageLocators.EDIT_INFO))

    def auth_login_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text
