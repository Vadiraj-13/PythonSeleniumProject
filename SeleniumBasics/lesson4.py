from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Index.html')

email = driver.find_element(By.ID, 'email')
email.send_keys('test@gmail.com')
driver.find_element(By.ID, 'enterimg').click()
driver.maximize_window()

select_web_element = driver.find_element(By.ID, 'Skills')

sel = Select(select_web_element)

# Select by index
sel.select_by_index(5)

# Select by value
sel.select_by_value('Configuration')

# Select by visible text
sel.select_by_visible_text('Configuration')
driver.get('https://www.google.com')
driver.back()
driver.refresh()
driver.forward()
print(driver.current_url)

driver.quit()
