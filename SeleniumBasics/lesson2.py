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

# //tag[@attribute='value']
driver.find_element(By.XPATH, "//*[@placeholder='First Name']")

# //*[text()='']
# //*[contains(text(),'')]

# //*[@placeholder='First Name' and/or @ng-model='FirstName']

# //label[1]
# //form[@id='basicBootstrapForm']//child::div
# //form[@id='basicBootstrapForm']//parent::div
# //form[@id='basicBootstrapForm']//ancestor::div
# //input[@id='checkbox1']//following-sibling::label
# //label[text()=' Cricket ']//preceding-sibling::input

driver.quit()
