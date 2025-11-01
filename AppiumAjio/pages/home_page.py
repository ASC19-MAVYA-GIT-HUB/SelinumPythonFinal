from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "searchVal")

    def search_product(self, product_name):
        search = self.driver.find_element(*self.search_box)
        search.clear()
        search.send_keys(product_name)
        search.send_keys(Keys.RETURN)