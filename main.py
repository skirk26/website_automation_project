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
def check_presence(element):
    wait.until(EC.presence_of_element_located((By.ID, element)))
def send_keys(element, key):
    wait.until(EC.element_to_be_clickable((By.ID, element))).send_keys(key)

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)

driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys('secret_sauce')
driver.find_element(By.ID, "login-button").click()
click("add-to-cart-sauce-labs-backpack")
click("add-to-cart-sauce-labs-bolt-t-shirt")
click("shopping_cart_container")
check_presence('checkout')
click("checkout")
check_presence('first-name')
send_keys('first-name', 'John')
check_presence('last-name')
send_keys('last-name', 'Doe')
check_presence('postal-code')
send_keys('postal-code', '123456')
check_presence('continue')
click("continue")
driver.quit()

