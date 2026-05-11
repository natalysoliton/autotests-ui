from playwright.sync_api import expect, sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('natsol@mail.ru')

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('natsol')

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('1qaz!qaz')

    # Нажимаем на кнопку Registration
    button = page.get_by_test_id('registration-page-registration-button')
    button.click()

    # Проверяем, что появился текст Dashboard после успешной регистрации
    dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_text).to_be_visible()
    expect(dashboard_text).to_have_text('Dashboard')
