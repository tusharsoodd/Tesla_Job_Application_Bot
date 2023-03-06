import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC


def InternshipFormFiller(link):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)


    # wait = WebDriverWait(browser, 10)
    # element=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/form/div/main/div/div/table/tbody/tr[1]/td[1]/a')))

    # WebDriverWait(browser, 5).until(browser.find_element(By.XPATH,'//*[@id="app"]/div/form/div/main/div/div/table/tbody/tr[1]/td[1]/a'))
    # links=browser.find_element(By.XPATH,'//*[@id="app"]/div/form/div/main/div/div/table/tbody/tr[1]/td[1]/a')

    # time.sleep(2)

    # try:
    #     links = browser.find_element(By.XPATH, '//*[@id="app"]/div/form/div/main/div/div/table/tbody/tr[1]/td[1]/a')
    #     links.click()
    #
    # except(selenium.common.exceptions.StaleElementReferenceException):
    #     links = browser.find_element(By.XPATH, '//*[@id="app"]/div/form/div/main/div/div/table/tbody/tr[1]/td[1]/a')
    #     links.click()


    # for link in links[0:]:
    time.sleep(1)


    # browser.implicitly_wait(3)
    apply_button=browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/a")   ###
    browser.execute_script("arguments[0].click();", apply_button)

    parent = browser.window_handles[0]
    chld = browser.window_handles[1]
    browser.switch_to.window(chld)

    browser.maximize_window()

    time.sleep(2)
    #Getting fields
    browser.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[2]/div[1]/input").send_keys("Sood")

    # time.sleep(3)

    browser.find_element(By.NAME, "personal.firstName").send_keys("Tushar")
    browser.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[5]/div/div/div/button").click()
    browser.find_element(By.ID, "country-listbox-GB").click()
    time.sleep(2)
    # countryCodeList=countryCode.find_elements(By.TAG_NAME, "li")
    # for code in countryCodeList:
    #     if code.text == "GB +44":
    #         code.click()


    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "personal.phone")))
    Select(browser.find_element(By.NAME, "personal.phoneType")).select_by_value("mobile")  ##dropdown
    browser.find_element(By.NAME,"personal.email").send_keys("s2134605@ed.ac.uk")
    browser.find_element(By.NAME, "personal.phone").send_keys("7774953280")
    Select(browser.find_element(By.NAME, "personal.country")).select_by_value('US') ##dropdown


    browser.find_element(By.CLASS_NAME, "tds-form-input-file-upload").send_keys("C://Users/91931/Downloads/Sood Tushar Resume Mk 2c.pdf")

    time.sleep(2)

    #click next
    browser.execute_script("arguments[0].click();", browser.find_element(By.NAME, "next"))

    time.sleep(1)


    #picking date
    waitFor2ndPage=WebDriverWait(browser,5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "job.jobAvailabilityToStartInternship")))
    waitFor2ndPage.click()

    # browser.execute_script("arguments[0].click();", browser.find_element(By.NAME, "job.jobAvailabilityToStartInternship"))

    browser.execute_script("arguments[0].click();", browser.find_element(By.XPATH, '//*[@id="step--job"]/fieldset/div[1]/div/div[1]/div[2]/div/div[3]/button[25]'))

    # browser.find_element(By.XPATH, '//*[@id="step--job"]/fieldset/div[1]/div/div[1]/div[2]/div/div[3]/button[25]').click()

    Select(browser.find_element(By.NAME, "job.jobInternshipDuration")).select_by_value("7_months_or_more")  ##dropdown
    Select(browser.find_element(By.NAME, 'job.jobInternshipType')).select_by_value("full_time")  ##dropdown

    time.sleep(2)
    radioB=WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset/div[4]/div/div[1]/div[2]/input')))
    browser.execute_script("arguments[0].scrollIntoView()", radioB)
    browser.execute_script("arguments[0].click()", radioB)

    # radioB.click()
    #Take the one with the value no

    # time.sleep(2)

    time.sleep(2)
    #click next
    browser.execute_script("arguments[0].click();", browser.find_element(By.NAME, "next"))


    time.sleep(2)

    noticP=WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "legal.legalNoticePeriod")))
    Select(noticP).select_by_value("3_4_weeks")
    # Select(browser.find_element(By.NAME, "legal.legalNoticePeriod")).select_by_value("3_4_weeks")  ##dropdown
    futureopps=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[2]/div/div[1]/div[1]/input')
    browser.execute_script("arguments[0].click();", futureopps)

    immigration=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[3]/div/div[1]/div[2]/input')
    browser.execute_script("arguments[0].click();", immigration)

    prevTesla=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[4]/div/div[1]/div[2]/input')
    browser.execute_script("arguments[0].click();", prevTesla)

    formerIntern=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[5]/div/div[1]/div[2]/input')
    browser.execute_script("arguments[0].click();", formerIntern)

    currentUniStudent=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[6]/div/div[1]/div[1]/input')
    browser.execute_script("arguments[0].click();", currentUniStudent)


    # time.sleep(2)
    buttone = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "legal.legalUniversityAnticipatedGraduationDate")))
    # browser.find_element(By.NAME, "legal.legalUniversityAnticipatedGraduationDate").click()

    browser.execute_script("arguments[0].click();", buttone)


    i=0
    while i<16:
        clicker = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[1]/button[2]')))
        browser.execute_script("arguments[0].click();", clicker)
        i+=1

    # time.sleep(1)

    nextButton=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[3]/button[7]')))
    browser.execute_script("arguments[0].click();", nextButton)

    # time.sleep(1)
    # browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[3]/button[7]').click()

    receiveNotification=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, 'legal.legalReceiveNotifications')))
    browser.execute_script("arguments[0].click();", receiveNotification)


    # browser.find_element(By.NAME, 'legal.legalReceiveNotifications').click()
    browser.execute_script("arguments[0].click();", browser.find_element(By.NAME, 'legal.legalAcknowledgment'))


    browser.find_element(By.NAME, "legal.legalAcknowledgmentName").send_keys("Tushar Sood")

    # time.sleep(2)
    browser.execute_script("arguments[0].click();", browser.find_element(By.NAME, "next"))
    time.sleep(2)

    ##Page 3: Scrolling down
    scrollableDiv=browser.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[1]/div/div[5]/p[2]')

    browser.execute_script("arguments[0].scrollIntoView(true);", scrollableDiv)
    # browser.execute_script("window.scrollTo(50);")

    time.sleep(5)

    last_check=browser.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[2]/div[1]/input")

    browser.execute_script("arguments[0].click();", last_check)

    # browser.find_element(By.NAME, "eeo.eeoAcknowledgment").click()

    Select(browser.find_element(By.NAME, "eeo.eeoGender")).select_by_value("male")  ##dropdown
    Select(browser.find_element(By.NAME, "eeo.eeoVeteranStatus")).select_by_value("no")  ##dropdown
    Select(browser.find_element(By.NAME, "eeo.eeoRaceEthnicity")).select_by_value("asian")  ##dropdown
    Select(browser.find_element(By.NAME, "eeo.eeoDisabilityStatus")).select_by_value("no")  ##dropdown

    browser.find_element(By.NAME, "eeo.eeoDisabilityStatusName").send_keys("Tushar Sood")

    submitButton=WebDriverWait(browser,5).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[2]/button[2]")))
    browser.execute_script("arguments[0].click();", submitButton)
    time.sleep(3)

    browser.quit()
