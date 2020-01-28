
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver

#import unittest

from screenshot import screenshot
from filters import filters
from headerSearch.headerSearch import headerSearch
from searchResults import searchResults


class challenge2(unittest.TestCase):

    def setUp(self):
        print('in setup method')
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
#        self.assertIn("Copart", self.driver.title)
        print ('setup in process')

    def tearDown(self):
        self.driver.close()
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
        searchterm = "exotic"
        print ('go to copart')
        self.driver.get("https://www.copart.com")
#        searchfield = self.driver.find_element(By.ID, "input-search")
#        searchfield.send_keys("exotic")
#        searchbutton = self.driver.find_element(By.XPATH, "//button[@data-uname=\"homepageHeadersearchsubmit\"]")
#        searchbutton.click()
#        dataelement = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody"))
#        dataelement = WebDriverWait(self.driver, 60).until(EC.visibility_of((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
#        html = dataelement.get_attribute("innterHTML")
#        print(html);

#        self.assertIn("PORSCHE", html)

    def test_challenge6(self):
        headerSearch()
        hs = headerSearch()
#        hs = headerSearch(self.driver)
        hs.searchFor("nissan")
        f = filters()
        f.clickFilter("Model")
        s = screenshot()
        s.takeScreenshot("Skyline")
        sr = searchResults()
        sr.changeDropDown("100")

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
