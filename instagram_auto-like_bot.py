#open Google
from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver')
#open instagram login page
browser.get('https://www.instagram.com/')
time.sleep(2)
#give my email
ubox=browser.find_element_by_name("username")
ubox.send_keys(em) # save your mail id in em

#give my password
pbox=browser.find_element_by_name("password")
pbox.send_keys(pwd) # save your password in pwd

#click on log in button
btn= browser.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
btn.click()
time.sleep(3)
#open link of the target person
browser.get('https://www.instagram.com/vickykaushal09/')
time.sleep(5)
#open latest post
browser.find_element_by_xpath('//div[@class="_ac7v _aang"]/div[1]/a').click()
time.sleep(2)
#check if already liked
try:
	browser.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
	print('Liked!!')
except:
	print('No New Posts')
#if not, like by clicking the button
