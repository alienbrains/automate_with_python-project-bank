from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.text import MIMEText
import os 

city='' #Enter your city name
query= 'weather in ' + city
print(query)
browser=webdriver.Chrome('chromedriver')
browser.get('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjQ3oHZkrL6AhVFR2wGHenUCHoQPAgI')
box=browser.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
box.send_keys(query)
box.send_keys(Keys.ENTER)

w_c=browser.find_element_by_xpath('//span[@id="wob_dc"]').text
print(w_c)

t=browser.find_element_by_xpath('//span[@id="wob_tm"]').text
print(t)

h=browser.find_element_by_xpath('//div[@class="wtsRwe"]/div[2]/span').text
print(h)

w=browser.find_element_by_xpath('//div[@class="wtsRwe"]/div[3]/span/span[1]').text
print(w)

msg = " The weather condition in " + city + " is going to be "+w_c + " today. \n The temperature will be "+ t + " in celcius.\n The wind speed will be "+ w+".\n The humidity will be "+ h+"."


# Automated mail sending
sender = ''#Enter your mail id
pas = '' #Enter your password
tar = '' #Enter ythe receiver's mail id
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, pas)

msg=MIMEText(msg)

msg['Subject'] ='Weather Update'
msg['From'] = sender
msg['To'] = tar

server.sendmail(sender, tar, msg.as_string())
server.quit()

print('DONE')
