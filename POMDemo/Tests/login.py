import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "span.oxd-userdropdown-tab").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed Successfully")

if __name__=="__main__":
    unittest.main()







