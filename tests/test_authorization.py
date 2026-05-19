import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),  # два пробела
        ("  ", "password"),              # два пробела
    ],
    ids=[
        "Invalid email and password",
        "Invalid email and empty password",
        "Empty email and invalid password",
    ]
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    # Открываем страницу логина
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле Email параметризованным значением
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    # Заполняем поле Password параметризованным значением
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    # Нажимаем кнопку Login
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверяем наличие и текст алерта
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
