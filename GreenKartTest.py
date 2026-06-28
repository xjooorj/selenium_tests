import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h4.product-name"))
)

products = driver.find_elements(By.CSS_SELECTOR, ".product")
for product in products:
    name = product.find_element(By.CSS_SELECTOR, ".product-name").text

    if "Cucumber" in name:
        for _ in range(10):
            product.find_element(By.CLASS_NAME, "increment").click()

        product.find_element(By.TAG_NAME, "button").click()
        break

for product in products:
    name = product.find_element(By.CSS_SELECTOR, ".product-name").text

    if "Beans" in name:
        for _ in range(3):
            product.find_element(By.CLASS_NAME, "increment").click()

        product.find_element(By.TAG_NAME, "button").click()
        break

driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
driver.find_element(By.CSS_SELECTOR, "div.action-block button").click()
WebDriverWait(driver, 10).until(
    EC.url_contains("cart")
)
buttons = driver.find_elements(By.CSS_SELECTOR, "div.products button")
buttons[-1].click()

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select"))
dropdown.select_by_visible_text("Uzbekistan")
driver.find_element(By.CSS_SELECTOR, "input[class = 'chkAgree']").click()
driver.find_element(By.TAG_NAME, "button").click()



#driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("pumpkin")

time.sleep(4)


