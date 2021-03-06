
# -*- coding: utf-8 -*-
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#import time, unittest

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)



#import unittest, time, re
#from selenium import webdriver

class challenge8(unittest.TestCase):

    def setUp(self):
        print('in setup method')
        dict = {'port': 8090}
        self.server = Server(path="C:\\Users\\SlingUserB\\PycharmProjects\\challenges\\test1\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy", options=dict)
        self.server.start()
        time.sleep(1)
        self.proxy = self.server.create_proxy()
        time.sleep(1)
        profile = webdriver.FirefoxProfile()
        selenium_proxy = self.proxy.selenium_proxy()
        profile.set_proxy(selenium_proxy)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver = webdriver.Firefox("../geckodriver.exe")
#        self.driver = webdriver.Chrome("../chromedriver.exe")
##        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()
        self.server.stop()
        print ('in tear down method')

#    def test_challenge3forloop(self):
#        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]div[1]//a")
#        for count in elements:
#            print(count.text + ": " + count.get_attribute("href"))

#        self.challenge3whileloop()

#    def challenge3whileloop(self):
#        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"popularSearches\"]/..div[3]//a")
#        i = 0
#        while i< len(elements):
#            print(elements[i].text + ": " + elements[i].get_attribute("href"))
#            i +=1


    def test_challenge2(self):
        self.proxyy.new_har("copart")
        searchterm = "exotic"
        print ('go to copart')
        self.driver.get("https://www.copart.com")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("exotic")
        searchbutton = self.driver.find_element(By.XPATH, "//button[@data-uname=\"homepageHeadersearchsubmit\"]")
        searchbutton.click()
        datawait.WebDriver(self.driver, 30)
        datawait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
        data = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]")
        html = data.text
        self.proxy.har

        for entry in self.proxy.har['log']['entries']:
            _url = entry['request']['url']
            _response = entry['response']
            print(_url)
            print(_response)
#        dataelement = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody"))
#        dataelement = WebDriverWait(self.driver, 60).until(EC.visibility_of((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
#        html = dataelement.get_attribute("innterHTML")
#        print(html);

        self.assertIn("PORSCHE", html)

#    def test_challenge6(self):
#        try:
#            filterName = "Model"
#            modelvalue = "Altima SE"
#            elements = self.driver.find_elements("//*[@id='filters-collapse-1']//li//a/text()")
#            count =3
#            for e in elements:
#                count = count + 1
#                if (e.text ==filterName):
#                    e.click()
#            txtelement = self.driver.find_element("//*[@id='collapseinside" + str(count) + "']/form/div/input")
#            txtelement.send_keys(modelvalue)
#            checkElement = self.driver.find_element("//*[@id='collapseinside4" + str(count) + "']//abbr[@value='" + modelvalue + "']")
#            checkElement.click()
#        except:
#            print("An exception occured")
#            print ("you wanted " + modelvalue)
#            gac = GetAllCheckboxes()
#            gac.show()
#            checkboxelements = self.driver.find_elements("// *[@id='collapseinside4']//input[@type='checkbox']")
#            print (" but these are the availabe checkboxes")
#            for e in checkboxelements:
#                e.get_attribute("value")

if __name__ == "__main__":
    unittest.main()
