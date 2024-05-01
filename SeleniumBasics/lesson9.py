import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://magento.softwaretestingboard.com/')
driver.implicitly_wait(3)
driver.maximize_window()

women = driver.find_element(By.XPATH, '//*[@id="ui-id-4"]')

action = ActionChains(driver)
tops = driver.find_element(By.XPATH, '//*[@id="ui-id-9"]')
action.move_to_element(women).perform()
jackets = driver.find_element(By.XPATH,'//*[@id="ui-id-11"]')
action.move_to_element(tops).perform()
action.click(jackets).perform()

search = driver.find_element(By.ID,'search')

action.click(search).key_down(Keys.SHIFT).send_keys('Test').key_up(Keys.SHIFT).perform()
action.key_down(Keys.ENTER).perform()
time.sleep(5)
driver.quit()