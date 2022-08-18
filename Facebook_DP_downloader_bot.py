from selenium import webdriver
import urllib.request,time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://mbasic.facebook.com/rijit.chakraborty.5')
time.sleep(2)
dp = driver.find_element_by_xpath("//img[@class='bt_img']")
dp_link = dp.get_attribute('src')
urllib.request.urlretrieve(dp_link,'dp.jpg')


