from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Создаем элементы бокового меню
        self.dashboard_item = SidebarListItemComponent(page)
        self.courses_item = SidebarListItemComponent(page)

    def check_visible(self):
        """Проверяет отображение бокового меню"""
        self.dashboard_item.check_visible(name='dashboard', expected_text='Dashboard')
        self.courses_item.check_visible(name='courses', expected_text='Courses')

    def click_dashboard(self):
        """Нажимает на пункт меню Dashboard"""
        self.dashboard_item.click(name='dashboard')

    def click_courses(self):
        """Нажимает на пункт меню Courses"""
        self.courses_item.click(name='courses')