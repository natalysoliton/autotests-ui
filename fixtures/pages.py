import pytest
from playwright.sync_api import Page
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def dashboard_page_with_state(page: Page) -> DashboardPage:
    """Фикстура для дашборда с предварительной авторизацией"""
    return DashboardPage(page)


@pytest.fixture
def courses_list_page(page: Page) -> CoursesListPage:
    return CoursesListPage(page)


@pytest.fixture
def create_course_page(page: Page) -> CreateCoursePage:
    return CreateCoursePage(page)