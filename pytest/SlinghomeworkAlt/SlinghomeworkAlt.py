# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver


class SlingAltTagHW(unittest.TestCase):

    divCount = 0
    divAltCount = 0
    imageCount = 0
    imageAltCount = 0
    ahrefCount = 0
    ahrefAltCount = 0

    def setUp(self):
        print ('in setup method')
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.sling.com")

    def tearDown(self):
        self.driver.close()
        print ('in tear down method')

    def test_slingforAltTags(self):
        time.sleep(6)
        elements = self.driver.find_elements(By.XPATH, "//*")
        print ("length " + str(len(elements)))

        if e.tag_name == "div":
            self.divCount +=1
            if e.get_attribute("alt") !="":
                if e.get_attribute("alt") != None:
                    self.divAltCount += 1
                    print(e.get_attribute("alt"))
            if e.tag_name == "a":
                self.ahrefCount+= 1
                if e.get_attribute("alt") != "":
                    if e.get_attribute("alt") != None:
                        self.ahrefAltCount += 1
                        print(e.get_attribute("alt"))
            tags.append(e.tag_name)
        tags.sort()
        print("total divs: " + str(self.divCount))
        print("total divs with Alt: " + str(self.divAltCount))
        print("total img: " + str(self.imageCount))
        print("total img with Alt: " + str(self.imageAltCount))
        print("total ahref: " + str(self.ahrefCount))
        print("total ahref with Alt: " + str(self.ahrefAltCount))

if __name__ == ' __main__':
        unittest.main()
