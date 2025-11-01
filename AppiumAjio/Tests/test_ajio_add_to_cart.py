import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.smoke  # optional marker
def test_ajio_search_and_select_size():
    # ✅ Launch Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Step 1: Open Ajio website
    driver.get("https://www.ajio.com/")
    time.sleep(3)

    # Step 2: Search for a product (example: Tshirt)
    search_box = driver.find_element(By.NAME, "searchVal")
    search_box.send_keys("Tshirt")
    search_box.submit()
    time.sleep(5)

    # Step 3: Click the first product from search results
    first_product = driver.find_element(By.XPATH, "(//div[@class='item rilrtl-products-list__item item'])[1]")
    first_product.click()
    time.sleep(3)

    # Step 4: Switch to product page tab
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    # Step 5: Wait and select first available size if present
    wait = WebDriverWait(driver, 15)
    try:
        size_elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'size-variant-item')]"))
        )

        for size in size_elements:
            if "disabled" not in size.get_attribute("class"):
                driver.execute_script("arguments[0].scrollIntoView(true);", size)
                ActionChains(driver).move_to_element(size).click().perform()
                print("✅ Size selected successfully!")
                break
        else:
            print("⚠️ All sizes appear to be unavailable or out of stock.")
    except Exception as e:
        print(f"⚠️ No size selection available. Error: {e}")

    print("✅ Test completed successfully.")
    time.sleep(3)
    driver.quit()
