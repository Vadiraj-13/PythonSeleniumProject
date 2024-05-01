from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Index.html')

email = driver.find_element(By.ID, 'email')
driver.find_element(By.ID, 'enterimg').click()
# Implicit Wait
# driver.implicitly_wait(2)
# driver.find_element(By.XPATH,'//*[@placeholder="First Name"]').send_keys("Vadiraj")


wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@placeholder="First Name"]'))).send_keys("Vadiraj")
