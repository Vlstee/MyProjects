from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH,'//input[@id="1"]')
        self.search_button = (By.XPATH,"//div[@class='search-icon-wrap ng-star-inserted']")

    def load(self):
        self.driver.get("https://www.mvideo.ru")

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
            return True
        except:
            return False


    def search_for_product(self,query):
        search_input = self.driver.find_element(*self.search_box)
        search_input.clear()
        search_input.send_keys(query)
        self.driver.find_element(*self.search_button).click()










