##import requests
##session=requests.Session()
##
##params = {'Email': 'hamzakhurshid123', 'password': 'khuljasimsim321','__RequestVerificationToken:':'CfDJ8ATf4Su878dOnC1xwa5QU5uDVHI_ZqcLdJN4CD2bcdeo8x8qqVGODVMXxjliIwQ2BwDHPHqhlvgHWAji74DWAuT5QcmyAzotOVXyHEDwPaeGmqAkavomVesp7C0VNUh_qgw2CFSXRgYyq8Jxorf_tTQ','RememberMe':'false'}
##r = session.post("https://sarahah.com/Account/Login", params)
##print("Cookie is set to:")
##print(r.cookies.get_dict())
##print("-----------")
##print("Going to profile page...")
##r = session.get("https://sarahah.com/messages")
##print(r.text)


##from requests import session
##
##payload = {
##    'action': 'login',
##    'username': 'hamzakhurshid123',
##    'password': 'khuljasimsim321'
##}
##
##with session() as c:
##    c.post('https://sarahah.com/Account/Login', data=payload)
##    response = c.get('https://sarahah.com/messages')
##    print(response.headers)
##    print(response.text)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time, winsound

driver = webdriver.Chrome()
count=0
file=open('working_accounts.txt','r+')
usernames=file.read().split('\n')
usernames=usernames[0:len(usernames)-1]
file.close()
for x in usernames:
    try:
        driver.get("https://www.sarahah.com/Account/Login")
        email=driver.find_element_by_name('Email')
        password=driver.find_element_by_name('Password')
        submit=clear_button = driver.find_elements_by_tag_name('button')[1]
        email.send_keys(x)
        password.send_keys('khuljasimsim321')
        submit.click()
        time.sleep(2)
        logout=driver.find_element_by_id('logoutForm')
        source=driver.page_source
        if not "You don't have any messages" in source:
            winsound.Beep(1000,3000)
            messages=open("Messages.txt","a+")
            messages.write(x+"/n")
            messages.close()
            print(x+" has a message for you")
        logout.click()
    except:
        print("Exception for: "+x)
        pass
driver.close()
print('Done Checking!')
