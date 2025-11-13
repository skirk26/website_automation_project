from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/Users/samkirkhorn/desktop/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
def click(element):
    wait.until(EC.element_to_be_clickable((By.ID, element))).click()
try:
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    driver.find_element(By.ID, "password").send_keys('secret_sauce')
    driver.find_element(By.ID, "login-button").click()
    click("add-to-cart-sauce-labs-backpack")
    input('test')
except:
    driver.quit()
