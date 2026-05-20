from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Добавляем компоненты
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Элементы страницы
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-button')

        # Элементы пустого состояния
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

        # Карточки курсов (если есть)
        self.course_cards = page.get_by_test_id('course-card')

    def check_visible_courses_title(self):
        """Проверяет отображение заголовка Courses"""
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_create_course_button(self):
        """Проверяет отображение кнопки создания курса"""
        expect(self.create_course_button).to_be_visible()

    def check_visible_empty_view(self):
        """Проверяет отображение пустого блока с сообщением об отсутствии курсов"""
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    def check_visible_course_card(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        """Проверяет отображение карточки курса с указанными данными"""
        course_card = self.course_cards.nth(index)

        title_element = course_card.get_by_test_id('course-card-title-text')
        expect(title_element).to_be_visible()
        expect(title_element).to_have_text(title)

        max_score_element = course_card.get_by_test_id('course-card-max-score-text')
        expect(max_score_element).to_be_visible()
        expect(max_score_element).to_have_text(max_score)

        min_score_element = course_card.get_by_test_id('course-card-min-score-text')
        expect(min_score_element).to_be_visible()
        expect(min_score_element).to_have_text(min_score)

        estimated_time_element = course_card.get_by_test_id('course-card-estimated-time-text')
        expect(estimated_time_element).to_be_visible()
        expect(estimated_time_element).to_have_text(estimated_time)

    def click_create_course_button(self):
        """Нажимает на кнопку создания курса"""
        self.create_course_button.click()
