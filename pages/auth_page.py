
from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Что мне надо:
# - чтобы заходил на страницу авторизации
# - чтобы были короткие команды на элементы
#   - нажимание на табы, ввод почты/логина, клик войти
# - определение активного таба
# - определение наличия на экране
#


class AuthPage(WebPage):
    def __init__(self, driver):

        super().__init__(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "standard_auth_btn"))).click()

        self.user = WebElement(self._driver,'id', "username")
        self.password = WebElement(self._driver, 'id', "password")
        self.enter = WebElement(self._driver, 'id', "kc-login")
        self.tab_phn = WebElement(self._driver, 'id', "t-btn-tab-phone")
        self.tab_mal = WebElement(self._driver, 'id', "t-btn-tab-mail")
        self.tab_log = WebElement(self._driver, 'id', "t-btn-tab-login")
        self.tab_ls = WebElement(self._driver, 'id', "t-btn-tab-ls")
        self.tab_text = WebElement(self._driver, 'css', "div.rt-input-container.tabs-input-container__login")
        self.tab_text_phn = "Мобильный телефон"
        self.tab_text_mal = "Электронная почта"
        self.tab_text_log = "Логин"
        self.tab_text_ls = "Лицевой счёт"
        self.logo = WebElement(self._driver, 'css', "div.what-is-container")
