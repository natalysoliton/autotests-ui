import allure
import pytest
from allure_commons.types import Severity # Импортируем enum Severity из Allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
class TestCourses:

    @allure.title("Check displaying of empty courses list")  # Добавили заголовок
    @allure.severity(Severity.NORMAL)  # Добавили severity
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        """Тест проверяет отображение пустого списка курсов"""
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Check displaying of empty courses list")  # Добавили заголовок
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        """Тест создания курса с упражнением"""
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

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

        # Проверка блока упражнений (пустое состояние)
        create_course_page.exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

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

    @allure.title("Edit course")  # Добавили заголовок
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        """
        Тест редактирования курса:
        1. Создание нового курса
        2. Редактирование всех полей курса
        3. Проверка обновленных данных
        """

        # ========== Шаг 1: Создание курса ==========
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Загрузка изображения для курса
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Заполнение формы создания курса
        create_course_page.create_course_form.fill(
            title="Original Course",
            estimated_time="1 week",
            description="Original description",
            max_score="50",
            min_score="5"
        )

        # Проверка пустого состояния упражнений
        create_course_page.exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        # Создание курса
        create_course_page.toolbar_view.click_create_course_button()

        # ========== Шаг 2: Проверка отображения созданного курса ==========
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Original Course",
            max_score="50",
            min_score="5",
            estimated_time="1 week"
        )

        # ========== Шаг 3: Редактирование курса ==========
        # Открываем меню карточки и нажимаем Edit
        courses_list_page.course_view.menu.click_edit(index=0)

        # ========== Шаг 4: Изменение всех полей курса ==========
        # Новые данные для курса
        updated_title = "Updated Course"
        updated_estimated_time = "3 weeks"
        updated_description = "Updated description after editing"
        updated_max_score = "200"
        updated_min_score = "20"

        # Загружаем новое изображение
        create_course_page.image_upload_widget.click_remove_image_button()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Заполняем форму обновленными данными
        create_course_page.create_course_form.fill(
            title=updated_title,
            estimated_time=updated_estimated_time,
            description=updated_description,
            max_score=updated_max_score,
            min_score=updated_min_score
        )

        # ========== Шаг 5: Сохранение изменений ==========
        create_course_page.toolbar_view.click_create_course_button()

        # ========== Шаг 6: Проверка обновленных данных ==========
        # Проверяем, что карточка курса отображается с обновленными данными
        courses_list_page.course_view.check_visible(
            index=0,
            title=updated_title,
            max_score=updated_max_score,
            min_score=updated_min_score,
            estimated_time=updated_estimated_time
        )

        # Дополнительная проверка: убеждаемся, что старые данные не отображаются
        # (проверяем, что нет курса со старым названием)
        with pytest.raises(AssertionError):
            courses_list_page.course_view.title.check_have_text(
                "Original Course",
                nth=0
            )