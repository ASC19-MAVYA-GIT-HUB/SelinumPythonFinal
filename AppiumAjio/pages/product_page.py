from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Updated XPath to handle variations
        self.add_to_bag_btn = (By.XPATH, "//div[contains(text(),'ADD TO BAG') or contains(text(),'Add to Bag')]")

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            button = wait.until(EC.element_to_be_clickable(self.add_to_bag_btn))
            button.click()
            print("✅ Product added to cart successfully!")
        except Exception as e:
            print("❌ Could not click 'Add to Bag' button. Error:", e)
            print("Trying again after small delay...")
            time.sleep(3)
            # Scroll and retry once
            self.driver.execute_script("window.scrollBy(0, 400);")
            button = wait.until(EC.element_to_be_clickable(self.add_to_bag_btn))
            button.click()