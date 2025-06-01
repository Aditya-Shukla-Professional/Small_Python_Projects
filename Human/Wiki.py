from selenium import webdriver
from selenium.webdriver.common.by import By

link="https://en.wikipedia.org/wiki/Main_Page"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(link)

article_num=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
article_num.click()
print(article_num.text)


driver.quit()
