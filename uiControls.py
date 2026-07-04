from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

buttons = driver.find_elements(By.XPATH, "//input[@class = 'radioButton']")
for button in buttons:
    if button.get_attribute('value') == "radio1":
        button.click()
        assert button.is_selected()
        break
#Needs fixing
#driver.find_element(By.ID, "autocomplete").send_keys("Uzbekistan")
#driver.find_element(By.CSS_SELECTOR, "input [name = 'enter-name']").send_keys("khojiakbar")
#driver.find_element(By.ID, "confirmbtn").click()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(3)