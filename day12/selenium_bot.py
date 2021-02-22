driver_path ="day12/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(driver_path)
driver.get("https://www.github.com/HakkiAkut")
driver.maximize_window()
driver.save_screenshot("day12/ss.png")
print(driver.title)
#driver.back() returns previous page
driver.get("https://github.com/HakkiAkut/python-learning")
# rather than using find_element_by_class_name,  
# doing it with xpath is better imo because we can search for multiple classes
h1 = driver.find_element_by_xpath("//*[@class=' d-flex flex-wrap flex-items-center break-word f3 text-normal']") 
print(h1.text)
driver.get("https://www.youtube.com")
video_title= driver.find_element_by_id("video-title") # will get first video title
print(video_title.text) # video title
video_channel= driver.find_element_by_xpath("//*[@id='metadata']/div/ytd-channel-name/div/div/yt-formatted-string/a")
print(video_channel.text) # video channel name

videos=driver.find_elements_by_id("video-title")
channels=driver.find_elements_by_xpath("//*[@id='metadata']/div/ytd-channel-name/div/div/yt-formatted-string/a")

print(videos)
print(channels)

for x in videos:
    print(x.text)

py=driver.get("https://www.python.org")

py_names=driver.find_elements_by_id(".blog-widget li a")
py_times=driver.find_elements_by_css_selector(".blog-widget time")

for i in py_times:
    print(i.text)

for x in py_names:
    print(x.text)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
link= driver.find_elements_by_xpath("//*[@id='articlecount']/a")[0]
link.click()

search= driver.find_element_by_name("search")
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)