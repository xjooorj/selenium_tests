import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("george")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()