from typing import Pattern
from playwright.sync_api import Page, expect
import allure # Импортируем allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):  # Добавили allure.step
            "Переход на страницу по URL"
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):  # Добавили allure.step
            "Перезагрузка страницы"
        self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):  # Добавили allure.step
            "Проверка текущего URL"
        expect(self.page).to_have_url(expected_url)