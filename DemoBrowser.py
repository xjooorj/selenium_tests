import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://hdrezka.today/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
