from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(3)
log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()

time.sleep(3)
facebook_button = driver.find_element(By.XPATH, '//*[@id="s1903812341"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_button.click()

time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(4)
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys(YOUR-EMAIL)
password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys(YOUR-PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(20)
location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
location.click()


time.sleep(20)
notifications = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()

time.sleep(5)
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

try:
    time.sleep(7)
    dark_mode = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button')
    dark_mode.click()

except NoSuchElementException:
    print("No dark mode, skipped.")

time.sleep(20)

for n in range(10):
    time.sleep(2)
    print("called")
    like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    like_button.click()


time.sleep(10)
driver.quit()