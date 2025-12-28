
#Что мне надо:
# - находит себя find_element(By.ID, '') - find() - element
from selenium.webdriver.common.by import By
# - видит что есть на экране EC.visibility_of_element_located((By.ID, "myDynamicElement")) - is_visible() - True/False
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# - вводит текст (.find(), .click(), .clear()? .send_keys('')) - input('')
# - кликает (.find(), .click()) - click()
#


class WebElement:
    def __init__(self, driver, method, key):
        """To use web element must use driver, method [id, name, class, xpath, css, link text, tag] and key"""

        self._driver = driver

        if method == "id":
            self._locate = By.ID, key
        elif method == "name":
            self._locate = By.NAME, key
        elif method == "class":
            self._locate = By.CLASS_NAME, key
        elif method == "xpath":
            self._locate = By.XPATH, key
        elif method == "css":
            self._locate = By.CSS_SELECTOR, key
        elif method == "link text":
            self._locate = By.LINK_TEXT, key
        elif method == "tag":
            self._locate = By.TAG_NAME, key

    def find(self):

        try:
            element = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((self._locate)))
        except:
            element = None
            print("Element not found")
        return element

    def is_visible(self):

        return EC.visibility_of_element_located((self._locate))

    def click(self):

        self.find().click()

    def input(self, keys):

        element = self.find()
        element.click()
        element.clear()
        element.send_keys(keys)