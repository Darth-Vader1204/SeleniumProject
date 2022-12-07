from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestSample:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//img[@class='oxd-userdropdown-img']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        x = driver.title
        assert x == "OrangeHRM"

# def test_teardown():
#     driver.close()
#     driver.quit()
#     print("Test Completed")
