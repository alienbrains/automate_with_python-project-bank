from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver')
browser.get('https://twitter.com/explore/tabs/trending')

time.sleep(5)
for i in range(3, 13):
	xpath=f'//div[@aria-label="Timeline: Explore"]/div/div[{i}]/div/div/div/div/div[2]/span/span'
	h=browser.find_element_by_xpath(xpath).text
	print(h)
