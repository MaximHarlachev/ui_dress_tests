from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.personal_data_page_locators import PersonalPageLocators


class PersonalDataPage(BasePage):
    def basic_data(self) -> WebElement:
        return self.find_element(PersonalPageLocators.BASIC_DATA)

    def name_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.NAME_INPUT)

    def lastname_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.LASTNAME_INPUT)

    def email_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.EMAIL_INPUT)

    def email_display_select(self) -> WebElement:
        email_display = self.find_select_element(PersonalPageLocators.EMAIL_DISPLAY)
        return email_display

    def moodle_net_profile_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.MOODLE_NET_PROFILE)

    def city_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.CITY_INPUT)

    def counry_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalPageLocators.COUNTRY_SELECT
        )
        return country_select

    def timezone_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalPageLocators.TIMEZONE_SELECT
        )
        return country_select

    def about_input(self) -> WebElement:
        return self.find_element(PersonalPageLocators.ABOUT)

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalPageLocators.SUBMIT_BUTTON)

    def input_name(self, name):
        self.fill_element(self.name_input(), name)

    def input_lastname(self, lastname):
        self.fill_element(self.lastname_input(), lastname)

    def input_email(self, email):
        self.fill_element(self.email_input(), email)

    def select_email_display(self, value):
        self.select_value(self.email_display_select(), value)

    def input_moodle_net_profile(self, url):
        self.fill_element(self.moodle_net_profile_input(), url)

    def input_city(self, city):
        self.fill_element(self.city_input(), city)

    def select_country(self, value):
        self.select_value(self.counry_select(), value)

    def select_timezone(self, value):
        self.select_value(self.timezone_select(), value)

    def input_about(self, text):
        self.fill_element(self.about_input(), text)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data(
        self,
        name="Макс",
        lastname="Харлачёв",
        email="negazirovannyi@inbox.ru",
        email_display_value="1",
        timezone="Europe/Moscow",
        moodle_net_profile="www.ya.ru",
        city="Питер",
        country="RU",
        text="Обо мне",
    ):
        self.input_name(name)
        self.input_lastname(lastname)
        self.input_email(email)
        self.select_email_display(email_display_value)
        self.input_moodle_net_profile(moodle_net_profile)
        self.input_city(city)
        self.select_country(country)
        self.select_timezone(timezone)
        self.input_about(text)
        self.submit_changes()

    def is_changed(self, wait_time=10):
        header_user_info_elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(PersonalPageLocators.NAVBAR_ITEMS),
            message=f"Can't find elements by locator "
            f"{PersonalPageLocators.NAVBAR_ITEMS}",
        )
        if len(header_user_info_elements) == 2:
            return True
        else:
            return False
