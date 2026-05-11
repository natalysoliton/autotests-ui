from playwright.sync_api import sync_playwright, expect

def test_registration_button_state():
    """
    Тест проверяет, что кнопка "Registration" разблокируется только после
    заполнения всех обязательных полей формы: Email, Username и Password.
    """
    with sync_playwright() as playwright:
        # Открываем браузер (headless=False - браузер будет виден на экране)
        browser = playwright.chromium.launch(headless=False)

        # Создаем новую вкладку (страницу)
        page = browser.new_page()

        # Переходим на страницу регистрации
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        print("Страница регистрации открыта")

        # Находим кнопку "Registration" по её data-testid атрибуту
        registration_button = page.get_by_test_id("registration-page-registration-button")

        # Проверяем, что кнопка изначально недоступна (disabled)
        # Ожидаем, что кнопка находится в состоянии disabled (серая, неактивная)
        expect(registration_button).to_be_disabled()
        print("Кнопка 'Registration' изначально disabled (недоступна)")

        # Заполняем поле Email
        # Находим поле ввода email по data-testid и получаем внутри него элемент input
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("user.name@gmail.com")  # Заполняем тестовым email
        print("Поле Email заполнено: user.name@gmail.com")

        # Заполняем поле Username (имя пользователя)
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username")  # Заполняем тестовым именем
        print("Поле Username заполнено: username")

        # Заполняем поле Password (пароль)
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password")  # Заполняем тестовым паролем
        print("Поле Password заполнено: password")

        # Проверяем, что кнопка стала доступной (enabled)
        # После заполнения всех полей кнопка должна разблокироваться
        expect(registration_button).to_be_enabled()
        print("Кнопка 'Registration' стала enabled (доступна для нажатия)")

        # Необязательная задержка для визуального наблюдения результата
        # Позволяет увидеть, что кнопка действительно стала активной
        print("Тест успешно завершен. Браузер закроется через 3 секунды...")
        page.wait_for_timeout(3000)



# Точка входа в программу
if __name__ == "__main__":
    """
    Запуск теста при прямом выполнении скрипта.
    Если скрипт импортируется как модуль, тест не запустится автоматически.
    """
    test_registration_button_state()
