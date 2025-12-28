

#Что мне надо:
# - определение url без параметров
#
#
#

class WebPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://start.rt.ru/')

    def get_url(self):
        """ Function to get url without suffix after '?' """
        url = self._driver.current_url.split('?')[0]
        return url