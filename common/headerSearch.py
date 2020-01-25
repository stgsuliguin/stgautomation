from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class headerSearch:
    def __init__(self, driver):
        self.driver = driver
        print("initializing headerSearch")

    def searchFor(self,query):
        print("search for " + query)
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys(query)
        searchbutton = self.driver.find_element(By.XPATH, "//button[@data-uname=\"homepageHeadersearchsubmit\"]")
        searchbutton.click()
        dataelement = WebDriverWait(self.driver, 60).until (EC.presence_of_element_located((By.XPATH, "//*[id=\"serverSideDataTable\"]//tbody")))
        html = dataelement.get_attribute("innerHTML")
        print(html);
