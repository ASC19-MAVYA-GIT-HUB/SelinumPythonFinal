from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product = (By.XPATH, "(//div[@class='nameCls'])[1]")

    def click_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_product)
        ).click()