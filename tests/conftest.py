import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state():
    """
    Фикстура для инициализации состояния браузера.
    Регистрирует нового пользователя и сохраняет состояние в файл.
    Выполняется один раз за сессию тестирования.
    """
    with sync_playwright() as playwright:
        # Открываем браузер
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переходим на страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поля регистрации
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Нажимаем кнопку регистрации
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера в файл
        context.storage_state(path="browser-state.json")

        # Закрываем браузер
        browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    """
    Фикстура для открытия страницы с сохранённым состоянием браузера.
    Использует файл browser-state.json для загрузки авторизованной сессии.
    Выполняется для каждого теста.
    """
    # Запускаем браузер с сохранённым состоянием
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    # Возвращаем страницу для использования в тесте
    yield page

    # Закрываем браузер после выполнения теста
    browser.close()
