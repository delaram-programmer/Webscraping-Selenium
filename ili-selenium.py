from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://e-ili.ir/Identity/Account/LogIn?ReturnUrl=%2F")
search1 = driver.find_element(By.ID,'Input_UserName')
search1.send_keys('9721000360',Keys.ENTER)
search2 = driver.find_element(By.ID,'password')
search2.send_keys('0929740408',Keys.ENTER)

search_url = "https://cb.meetingyar.com/Course_415467/?session=breezbreezdmcgag2b2mvn4mnc&proto=true"
driver.get(search_url)

button = driver.find_element(By.CLASS_NAME,"button-text")
button.click()

