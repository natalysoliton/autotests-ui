from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
import allure  # Импортируем allure

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')
        self.login_button = Button(page, 'login-page-login-button', 'Login')

    @allure.step("Fill login form")  # Добавили allure шаг
    def fill(self, email: str, password: str):
        """Заполняет форму с полями электронной почты и пароля"""
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step("Check visible login form")  # Добавили allure шаг
    def check_visible(self, email: str, password: str):
        """Проверяет корректность отображения формы и введённых данных"""
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

        self.login_button.check_visible()

    def click_login_button(self):
        """Нажимает кнопку входа"""
        self.login_button.click()