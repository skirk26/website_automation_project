from selenium import webdriver
from selenium.webdriver.common.keys import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/Users/samkirkhorn/desktop/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)