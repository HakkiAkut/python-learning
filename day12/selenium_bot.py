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
driver.get("https://github.com/HakkiAkut/python-learning")
# rather than using find_element_by_class_name,  
# doing it with xpath is better imo because we can search for multiple classes
h1 = driver.find_element_by_xpath("//*[@class=' d-flex flex-wrap flex-items-center break-word f3 text-normal']") 
print(h1.text)
time.sleep(1)
driver.get("https://www.youtube.com")
video_title= driver.find_element_by_id("video-title") # will get first video title
print(video_title.text) # video title
video_channel= driver.find_element_by_xpath("//*[@id='metadata']/div/ytd-channel-name/div/div/yt-formatted-string/a")
print(video_channel.text) # video channel name
driver.close()