#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By
#   Module to understand the test better #! Slows down the test result
# from time import sleep

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.minimize_window()
        driver.get('https://www.swissmedical.com.ar/prestadores')

    def test_login(self):
        driver = self.driver

        search_field = driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/div[1]/div[2]/div/div[1]/form/div[1]/input')
        search_field.clear()
        search_field.send_keys('optilog62@gmail.com')
        password_field = driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/div[1]/div[2]/div/div[1]/form/div[2]/input')
        password_field.clear()
        password_field.send_keys('')

    def test_connectivity_form(self):
        driver = self.driver

        driver.find_element(By.XPATH, "//a[@title='TRÁMITES CONECTIVIDAD']").click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)