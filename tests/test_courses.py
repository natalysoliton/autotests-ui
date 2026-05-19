import pytest
from playwright.sync_api import expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    """
    Тест проверяет отображение пустого списка курсов.
    Использует фикстуру courses_list_page для авторизованной сессии.
    """
    # Проверка заголовка "Courses"
    courses_list_page.check_visible_courses_title()

    # Проверка пустого блока
    courses_list_page.check_visible_empty_view()

    # Проверка кнопки создания курса
    courses_list_page.check_visible_create_course_button()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    """
    Тест проверяет создание нового курса.
    Использует фикстуры create_course_page и courses_list_page.
    """
    # Шаг 1: Открыта страница #/courses/create (фикстура уже открывает страницу)

    # Шаг 2: Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()

    # Шаг 3: Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()

    # Шаг 4: Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()

    # Шаг 5: Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

    # Шаг 6: Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    # Шаг 7: Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()

    # Шаг 8: Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()

    # Шаг 9: Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Шаг 10: Загрузить изображение для превью курса
    create_course_page.upload_preview_image("./testdata/files/image.png")

    # Шаг 11: Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # Шаг 12: Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Шаг 13: Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # Шаг 14: Проверить наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()

    # Шаг 15: Проверить наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()

    # Шаг 16: Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
