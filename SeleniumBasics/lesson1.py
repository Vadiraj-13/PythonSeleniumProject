from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Index.html')

email = driver.find_element(By.ID, 'email')
email.send_keys('test@gmail.com')
driver.find_element(By.ID, 'enterimg').click()

driver.quit()
