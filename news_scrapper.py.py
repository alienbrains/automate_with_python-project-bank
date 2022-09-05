from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

driver.get('https://timesofindia.indiatimes.com/news')
time.sleep(5)

for i in range(1,6):
    head = driver.find_element_by_xpath(f"//ul[@id='itemContainer']/li[{i}]/span/a").text
    print(head)