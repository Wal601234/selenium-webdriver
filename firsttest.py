from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

page_path = "file://" + os.path.abspath("index.html")
driver.get(page_path)

title = driver.title
assert title == "Custom Selenium Test Page"

driver.implicitly_wait(5)

text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

text_box.send_keys("Waleed")
submit_button.click()

message = driver.find_element(By.ID, "message")
value = message.text

print(value)

assert value == "Received: Waleed"

driver.quit()
