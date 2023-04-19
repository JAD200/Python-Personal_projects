#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
#   Find_element
from selenium.webdriver.common.by import By
#   Sensible data
from sensible import *
#   Expected conditions and explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#   Current date time selector
from current_datetime_selector import current_date
from time import sleep


class LoginTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(
            executable_path=ChromeDriverManager().install())
        options = ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        driver = self.driver
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        driver.implicitly_wait(6)
        driver.maximize_window()
        driver.get('https://bit.ly/3V2xSxz')

    def test_login(self):
        driver = self.driver
        # Log in
        mail_field = driver.find_element(
            By.NAME, "email")
        mail_field.clear()
        mail_field.send_keys(email_field_test)
        password_field = driver.find_element(
            By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password_field_test)
        password_field.submit()
        driver.implicitly_wait(10)
        # Select TRÁMITES CONECTIVIDAD
        # print('TRÁMITES CONECTIVIDAD')
        # connectivity_button = driver.find_element(
        # By.LINK_TEXT, "//a[@title='TRÁMITES CONECTIVIDAD']")
        # connectivity_button.click()
        current_date(driver)

        # Attention place
        driver.find_element(By.NAME, 'lugarDeAtencion').click()
        driver.implicitly_wait(1)
        driver.find_element(
            By.XPATH, "//option[text()='25 DE MAYO 910']").click()
        
        affiliate_number = driver.find_element(
            By.NAME, "validacionDelAfiliado")
        affiliate_number.send_keys(affiliate_number_test)
        driver.implicitly_wait(4)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
