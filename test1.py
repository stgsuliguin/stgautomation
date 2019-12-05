# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def browser():
    # Initialize ChromeDriver
    driver = Chrome()

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


class Asserttest1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/SlingUserB/PycharmProjects/challenges/challenge1/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_asserttest1(self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        content = driver.page_source
        driver.find_element_by_id("input-search").click()
        if driver.find_elements_by_id('input-search'):
            print("Element exists")
        self.assertTrue(self.is_element_present(By.ID, "time"))
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        driver.find_element_by_id("input-search").clear()
        elseYourMesg=driver.find_element_by_id("input-search").send_keys("exotics")
#        assert "time" in elseYourMesg
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Member Portal'])[1]/following::button[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PORSCHE'])[8]/following::span[1]").click()
        driver.find_element_by_xpath("//img[@alt='1986 PORSCHE 944 ']").click()
        if content.find("PORSCHE"):
            print("PORSCHE is present in the webpage")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
