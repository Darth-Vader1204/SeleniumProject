import time
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout_link()

        # driver.find_element(By.NAME, "username").send_keys("Admin")
        # driver.find_element(By.NAME, "password").send_keys("admin123")
        # driver.find_element(By.CSS_SELECTOR, "button[type=submit").click()
        # driver.find_element(By.CSS_SELECTOR, "span.oxd-userdropdown-tab").click()
        # driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(3)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()


