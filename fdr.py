from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumrequests import PhantomJS
import requests
import time

myUser = "";
myPass = "";

print("[+] Starting...")

# initiate
driver = webdriver.Firefox() # initiate a driver, in this case Firefox
driver.get("http://board.freedomainradio.com/chat") # go to the url

driver.find_element_by_css_selector('#sign_in').click()

wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ips_username")))

print("[+] Locating login window...")
# log in
username_field = driver.find_element_by_name("ips_username") # get the username field
password_field = driver.find_element_by_name("ips_password") # get the password field
print("[+] Logging in...")
username_field.send_keys(myUser) # enter in your username
password_field.send_keys(myPass) # enter in your password
password_field.submit() # submit it

print("[+] Agreeing to Molyneux's hugbox rules...")
driver.find_element_by_css_selector('.input_submit').click()
driver.find_element_by_css_selector('.input_submit').click()

html = driver.page_source

print("[+] Loading chat...")
time.sleep(5)
user = driver.find_elements_by_css_selector(".chat-message > label")
text = driver.find_elements_by_css_selector(".chat-message > div")
print("[+] Retrieving chat...")

for (u, t) in zip(user, text):
	try: 
		data = "text=" + t.text
		sentiment = requests.post('http://text-processing.com/api/sentiment/', data=data).json()
		print(u.text + ": " + t.text + ", Sentiment = " + sentiment["label"] + "\n")
	except:
		print("...")