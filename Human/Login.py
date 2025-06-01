from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link="https://secure-retreat-92358.herokuapp.com/"

chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome)
driver.get(link)

fName=driver.find_element(By.NAME,"fName")
fName.send_keys("Aditya")
lName=driver.find_element(By.NAME,"lName")
lName.send_keys("Shukla")
email=driver.find_element(By.NAME,"email")
email.send_keys("AdityaShukla@gmail.com")
email.send_keys(Keys.ENTER)
