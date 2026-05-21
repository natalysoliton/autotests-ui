import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    """Тест проверяет отображение пустого списка курсов"""
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    """Тест создания курса с упражнением"""

    # Проверка отображения тулбара (кнопка создания недоступна)
    create_course_page.toolbar_view.check_visible(is_create_course_disabled=True)

    # Проверка виджета загрузки изображения (без изображения)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    # Загрузка изображения
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполнение формы создания курса
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Course description",
        max_score="100",
        min_score="10"
    )

    # Проверка корректности заполнения формы
    create_course_page.create_course_form.check_visible(
        title="Playwright",
        estimated_time="2 weeks",
        description="Course description",
        max_score="100",
        min_score="10"
    )

    # Проверка блока упражнений (пустое состояние)
    create_course_page.exercises_toolbar_view.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    # Создание упражнения
    create_course_page.exercises_toolbar_view.click_create_exercise_button()
    create_course_page.create_exercise_form.fill(
        index=0,
        title="Exercise 1",
        description="Exercise description"
    )
    create_course_page.create_exercise_form.check_visible(
        index=0,
        title="Exercise 1",
        description="Exercise description"
    )

    # После заполнения всех полей и создания упражнения,
    # кнопка создания курса должна стать активной
    create_course_page.toolbar_view.check_visible(is_create_course_disabled=False)

    # Создание курса
    create_course_page.toolbar_view.click_create_course_button()

    # Проверка создания курса в списке
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )