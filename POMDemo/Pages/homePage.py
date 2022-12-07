from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_css_selector = "span.oxd-userdropdown-tab"
        self.logout_link_xpath = "//a[normalize-space()='Logout']"


    def click_welcome_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.welcome_link_css_selector).click()


    def click_logout_link(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()


