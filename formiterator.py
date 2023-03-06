import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from formfiller import InternshipFormFiller

FirstName="John"
LastName="Doe"
Email="john.doe@gmail.com"
PhoneNumber=9998767789

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.tesla.com/careers/search/?query=Internship&department=vehicle-software&site=US")

links=browser.find_elements(By.CLASS_NAME, "tds-link")
allLinks=[elem.get_attribute('href') for elem in links if elem.text.lower()!="about us"]

browser.quit()
for link in allLinks:
    InternshipFormFiller(link)
    with open('document.csv', 'a') as fd:
        fd.write(link)
    print(f"Successfully Applied to: {link}")
    fd.close()



# print(len(links))
# names={}
#
# for link in links:
#     print(link.text)
#     if len(link.text.split(" ")) > 2:
#         time.sleep(1)
#         link.click()
#         time.sleep(1)
#         # parent = browser.window_handles[0]
#         # chld = browser.window_handles[1]
#         # browser.switch_to.window(chld)
#         apply_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/a")  ###
#         browser.execute_script("arguments[0].click();", apply_button)
#
#         # names[link]= link.text


