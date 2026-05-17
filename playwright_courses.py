from playwright.sync_api import sync_playwright

# Константы для тестовых данных и URL
REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
DASHBOARD_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
COURSES_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
STORAGE_STATE_FILE = "browser-state.json"

TEST_EMAIL = "user.name@gmail.com"
TEST_USERNAME = "username"
TEST_PASSWORD = "password"


def test_courses_page_with_storage_state():
    with sync_playwright() as playwright:
        # ===== 1. РЕГИСТРАЦИЯ И СОХРАНЕНИЕ СОСТОЯНИЯ =====
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открываем страницу регистрации
        page.goto(REGISTRATION_URL)

        # Заполняем форму регистрации
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill(TEST_EMAIL)

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill(TEST_USERNAME)

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill(TEST_PASSWORD)

        # Нажимаем кнопку регистрации
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # 2. Ждём перехода на Dashboard и проверяем, что страница Dashboard открылась
        page.wait_for_url(DASHBOARD_URL, timeout=10000)
        assert page.url == DASHBOARD_URL, f"Открылась не Dashboard, а {page.url}"

        print("Страница Dashboard успешно открыта!")

        # Сохраняем состояние браузера (cookies + localStorage) после успешной авторизации
        context.storage_state(path=STORAGE_STATE_FILE)
        print(f"Состояние браузера сохранено в {STORAGE_STATE_FILE}")

        # Закрываем контекст и браузер после регистрации
        context.close()
        browser.close()

        # ===== 3. НОВАЯ СЕССИЯ С СОХРАНЁННЫМ СОСТОЯНИЕМ =====
        browser2 = playwright.chromium.launch(headless=False)
        # Подставляем сохранённое состояние при создании контекста
        context2 = browser2.new_context(storage_state=STORAGE_STATE_FILE)
        page2 = context2.new_page()

        # Открываем страницу Courses (должна открыться без авторизации)
        page2.goto(COURSES_URL)

        # Ждём появления заголовка Courses вместо networkidle
        page2.get_by_test_id('courses-list-toolbar-title-text').wait_for(state="visible", timeout=10000)

        # ===== 4. ПРОВЕРКИ НА СТРАНИЦЕ COURSES =====

        # Проверка заголовка "Courses"
        courses_header = page2.get_by_test_id('courses-list-toolbar-title-text')
        assert courses_header.is_visible(), "Заголовок 'Courses' не виден"
        assert courses_header.text_content().strip() == "Courses", \
            f"Неверный текст заголовка: {courses_header.text_content()}"

        # Проверка блока "There is no results"
        no_results_block = page2.get_by_text("There is no results")
        assert no_results_block.is_visible(), "Блок 'There is no results' не виден"
        assert no_results_block.text_content().strip() == "There is no results", \
            f"Неверный текст блока: {no_results_block.text_content()}"

        # Проверка иконки пустого блока
        empty_icon = page2.get_by_test_id("AddIcon")
        assert empty_icon.is_visible(), "Иконка пустого блока не видна"

        # Проверка описания блока
        description_block = page2.get_by_text("Results from the load test pipeline will be displayed here")
        assert description_block.is_visible(), "Описание блока не видно"
        assert description_block.text_content().strip() == "Results from the load test pipeline will be displayed here", \
            f"Неверный текст описания: {description_block.text_content()}"

        print("Все проверки на странице Courses успешно пройдены!")

        # Небольшая задержка, чтобы увидеть результат
        page2.wait_for_timeout(3000)

        # Закрываем браузер
        context2.close()
        browser2.close()


if __name__ == "__main__":
    test_courses_page_with_storage_state()
