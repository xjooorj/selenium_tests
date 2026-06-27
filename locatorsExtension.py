from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("12345678")
#driver.find_element(By.CLASS_NAME, "btn").click()
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()