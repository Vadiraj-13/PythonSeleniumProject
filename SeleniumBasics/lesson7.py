from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

#by id
# driver.switch_to.frame('singleframe')
#
# #by name
# driver.switch_to.frame('SingleFrame')
web_element = driver.find_element(By.XPATH, "//*[@id='Single']/iframe")
driver.switch_to.frame(web_element)
text = driver.find_element(By.TAG_NAME,'input')
text.send_keys('Vadiraj')

driver.switch_to.default_content()