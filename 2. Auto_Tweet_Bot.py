from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
driver.get('https://twitter.com/i/flow/login')
time.sleep(5)
driver.find_element_by_name('text').send_keys(' your username')
driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(5)
driver.find_element_by_name('password').send_keys('your password')
driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
time.sleep(3)
driver.find_element_by_xpath("//div[@role='textbox']").send_keys(' your message ')
time.sleep(3)
driver.find_element_by_xpath('//div[@data-testid="toolBar"]/div[2]/div[3]/div').click()
time.sleep(2)