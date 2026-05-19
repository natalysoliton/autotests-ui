from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локатор заголовка Dashboard
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    # Метод для проверки видимости и текста заголовка Dashboard
    def check_dashboard_title_visible(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text("Dashboard")
