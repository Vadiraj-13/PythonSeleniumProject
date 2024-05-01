import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()

# driver.find_element(By.XPATH, "//*[@class='btn btn-danger']").click()

driver.find_element(By.XPATH,"//*[@href='#Textbox']").click()
driver.find_element(By.XPATH, "//*[@class='btn btn-info']").click()
time.sleep(5)
# ok - accept
tx = driver.switch_to.alert.text
print(tx)
driver.switch_to.alert.send_keys('Vadiraj')

time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)

driver.quit()
