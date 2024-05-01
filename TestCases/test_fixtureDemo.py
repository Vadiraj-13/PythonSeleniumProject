import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def launchbrowser():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    yield
    driver.quit()

@pytest.fixture(scope="class")
def launchbrowser1(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(options=chrome_options)
    yield
    request.cls.driver.quit()

def test_printurl(launchbrowser):
    driver.get('https://demo.automationtesting.in/Datepicker.html')
    # print(driver.current_url)

def test_printurl1(launchbrowser):
    # driver.get('https://demo.automationtesting.in/Datepicker.html')
    print(driver.current_url)

@pytest.mark.usefixtures('launchbrowser1')
class Test_DatePicker:
    def test_entertheurl(self):
        self.driver.get('https://demo.automationtesting.in/Datepicker.html')

