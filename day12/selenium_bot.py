driver_path ="day12/chromedriver"
from selenium import webdriver
import time

driver = webdriver.Chrome(driver_path)
driver.get("https://www.github.com/HakkiAkut")
driver.maximize_window()
driver.save_screenshot("day12/ss.png")
time.sleep(2)
print(driver.title)
#driver.back() returns previous page
driver.close()