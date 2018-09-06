from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

driver = webdriver.Chrome()
driver.get("https://www.sarahah.com/Account/Register")
count=0
for x in range(0,100):
    count+=1
    print(str(count)+"% Completed")
    if not "Register" in driver.title:
        driver.back()
    file=open("accounts.txt",'a+')
    number=random.randint(0,99999)
    email0="email"+str(number)+'@sarahah-email.com'
    password0='khuljasimsim321'
    username0='hamzakhurshid'+str(number)
    file.write(username0+'\n')
    file.close()
    email = driver.find_element_by_name("Email")
    password = driver.find_element_by_name("Password")
    confirm = driver.find_element_by_name("ConfirmPassword")
    subdomain= driver.find_element_by_name("Subdomain")
    name = driver.find_element_by_name("Name")
    email.send_keys(email0)
    password.send_keys(password0)
    confirm.send_keys(password0)
    subdomain.send_keys(username0)
    print(username0)
    name.send_keys('Hamza K')
    driver.find_element_by_id("TermsCB").click() #Clicking on read and accept terms
    driver.find_element_by_id('RegisterBtn').click() #Clicking Register Button
    driver.find_element_by_id('logoutForm').click() #Loggingout
    driver.get("https://www.sarahah.com/Account/Register")
driver.quit()
