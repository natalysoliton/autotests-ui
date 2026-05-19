import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("test.user1@example.com", "testuser1", "Test123!"),
        ("test.user2@example.com", "testuser2", "SecurePass456"),
        ("test.user3@example.com", "testuser3", "StrongP@ss789"),
    ]
)
def test_successful_registration(
    registration_page: RegistrationPage,
    dashboard_page: DashboardPage,
    email: str,
    username: str,
    password: str
):
    """
    Тест успешной регистрации пользователя с параметризацией
    """
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title_visible()
