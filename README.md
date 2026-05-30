# UI Автотесты на Python и Playwright (курс https://stepik.org/lesson/1485902/step/2?unit=1505757)



Этот проект реализует автоматизированные тесты для учебного приложения [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). Тесты написаны с использованием **Python**, **Pytest**, **Allure** and **Playwright**. Исходный код тестового приложения доступен на [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Обзор проекта

Цель этого проекта — автоматизировать тестирование приложения UI Course. Автоматизированные тесты проверяют различные функции приложения, чтобы гарантировать его стабильность и корректность. Структура проекта соответствует лучшим практикам организации тестового кода с понятными и поддерживаемыми скриптами. В проекте применены следующие паттерны автоматизации: Page Object, Page Component и Page Factory. А также настроен запуск тестов в CI.

## Начало работы

### Клонирование репозитория

Для начала работы клонируйте репозиторий проекта с помощью Git:

```bash
git clone https://github.com/brizyriot/autotests-ui
cd autotests-ui
```

### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Следуйте инструкциям для вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\\\\Scripts\\\\activate
```

### Установка зависимостей

После активации виртуального окружения установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Дополнительная настройка Playwright 

Если вы запускаете Playwright впервые, может потребоваться установка браузеров:

```bash
playwright install
```

### Запуск тестов с генерацией отчёта Allure

Чтобы запустить тесты и сгенерировать отчёт Allure, используйте следующую команду:

```bash
pytest -m "regression" --alluredir=./allure-results
```

Эта команда выполнит все тесты в проекте и выведет результаты в терминал.

### Просмотр отчёта Allure

После выполнения тестов вы можете сгенерировать и открыть отчёт Allure с помощью команды:

```bash
allure serve allure-results
```

Эта команда откроет отчёт в вашем браузере по умолчанию.



