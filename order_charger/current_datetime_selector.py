#   find_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Current datetime
from datetime import date


def current_date(driver, date=date):
    try:
        # Click in the calendar
        calendar_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "fechaPrestacion")))
        calendar_element.click()
        # Identify div elements
        dates_divs = driver.find_elements(By.TAG_NAME, "div")
        # Iterate over divs
        today = date.today()
        current_date = str(today.day)
        for i in dates_divs:
            # Verify required date then click
            date = i.text
            if date == current_date:
                i.click()
                break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
