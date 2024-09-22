from base.base_page import BasePage


class Filters(BasePage):  # так же наследуемся от BasePage

    _TODAY_FILTER = "//span[text()='Today']"

    def click_today_filter(self):  # метод для работы элементом внутри компоненты
        self.driver.find_element(*self._TODAY_FILTER).click()

