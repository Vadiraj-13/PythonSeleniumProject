import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Datepicker.html')
driver.implicitly_wait(3)
driver.maximize_window()

select_date = "1-January-2014"

date = select_date.split('-')

driver.find_element(By.ID,'datepicker2').click()

# td = driver.find_elements(By.XPATH,"//div[@class='datepick']//td")
time.sleep(3)
select = Select(driver.find_element(By.XPATH,'//select[@title="Change the month"]'))
select.select_by_visible_text(date[1])

select = Select(driver.find_element(By.XPATH,'//select[@title="Change the year"]'))
select.select_by_visible_text(date[2])

# my_element_id = 'something123'
ignored_exceptions=('NoSuchElementException','StaleElementReferenceException')
td = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='datepick']//td" )))

for ele in td:
    if ele.text == date[0]:
        ele.click()
        time.sleep(4)
        break

driver.quit()


