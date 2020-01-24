
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
#self.driver = webdriver.Chrome(executable_path='C:/Users/SlingUserB/PycharmProjects/challenges/challenge1/chromedriver.exe')
#driver = webdriver.Chrome(chrome_options=options)
#driver.get('https://python.org')
#driver.save_screenshot("screenshot.png")
#driver.close()

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
        driver.get('https://python.org')
        driver.save_screenshot("screenshot.png")
        driver.close()


    def test_asserttest1(self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        content = driver.page_source
        driver.find_element_by_id("input-search").click()
        if driver.find_elements_by_id('input-search'):
            print("Element exists")
#        self.assertTrue(self.is_element_present(By.ID, "exotics"))
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=input-search | ]]
        driver.find_element_by_id("input-search").clear()
        elseYourMesg=driver.find_element_by_id("input-search").send_keys("exotics")
#        assert "time" in elseYourMesg
#        driver.find_element_by_xpath(
#            "(.//*[normalize-space(text()) and normalize-space(.)='Member Portal'])[1]/following::button[2]").click()
#        driver.find_element_by_xpath(
#            "(.//*[normalize-space(text()) and normalize-space(.)='PORSCHE'])[8]/following::span[1]").click()
#        driver.find_element_by_xpath("//img[@alt='PORSCHE']").click()
        if content.find("PORSCHE"):
            print("PORSCHE1 is present in the webpage")
#        if(driver.getPageSource().contains("PORSCHE"))
#           print("PORSCHE2 is present in the webpage")

    def test_challenge3forloop(self):
        print ('go to google')
        self.driver.get('https://www.copart.com')
#        elements = self.driver.find_element(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        elements =self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
#        elems = self.driver.find_elements_by_xpath("//*[@href]")
#x = str(continue_link)
#print(continue_link)
        for count in elements:
#            print(elem.get_attribute("href"))
            print(count.text + ": " + count.get_attribute("href"))

    def test_challenge3whileloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        i = 0
        while i < len(elements):
                print(elements[i].text + ": " + elements[i].get_attribute("href"))
                i += 1

    def test_challenge6trycatch(self):
        try:
            filterName = 'Model'
            modelsearch = 'altima'
            query = 'Nissan'
            self.driver.get("https://copart.com")
            headerSearch().search(self.driver, query)
            filter = Fliters()
            filter.searchFilterSection(self.driver, filterName)
            filter.searchFilterSection(self.driver, modelsearch)
            filter.clickFilterCheckbox(self.driver, modelsearch)

        except BaseException as e:
            Screenshot().take(self.driver, "challenge6")
            sys.exit(e)


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
