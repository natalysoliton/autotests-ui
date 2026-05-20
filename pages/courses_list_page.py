# Импортируем компонент
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы были заменены компонентом
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    # Методы были удалены, т.к. в автотестах будут использоваться методы компонента