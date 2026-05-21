from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_text = Text(page, 'navbar-user-info-username-text', 'Username')
        self.logout_button = Button(page, 'navbar-logout-button', 'Logout')

    def check_visible(self, username: str):
        """Проверяет отображение navbar с именем пользователя"""
        self.username_text.check_visible()
        self.username_text.check_have_text(username)

        self.logout_button.check_visible()

    def click_logout_button(self):
        """Нажимает кнопку выхода"""
        self.logout_button.click()