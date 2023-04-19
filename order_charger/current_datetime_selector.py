from selenium import webdriver
#   find_element
from selenium.webdriver.common.by import By
# Current datetime
from datetime import date


def current_date(driver, date=date):
    # Click in the calendar
    driver.find_element(By.NAME, "fechaPrestacion").click()
    # Identify div elements
    dates_table = driver.find_elements(By.TAG_NAME, "div")
    # Iterate over divs
    today = date.today()
    current_date = str(today.day)
    print(current_date)
    for i in dates_table:
        # Verify required date then click
        date = i.text
        print(date)
        if date == current_date:
            i.click()
            break
