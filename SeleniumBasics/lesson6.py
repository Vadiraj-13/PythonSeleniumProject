from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Windows.html')
driver.maximize_window()
parent = driver.current_window_handle

driver.find_element(By.XPATH, '//*[@href="http://www.selenium.dev"]').click()

lst = driver.window_handles

for ele in lst:
    print(ele)
    if ele != parent:
        driver.switch_to.window(ele)

driver.switch_to.window(parent)

driver.close()
