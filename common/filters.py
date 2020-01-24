class filters:
    sectionNum = 0
    def __init__(self,driver);
        self.driver = driver
        print ("init filters")

    def clickFilter(self, filterName):
        self.sectionNum = indexinloop
        print ("click on this filter name " + filterName)

    def filtersSearchText(self, filterBy):
        print("searching filter section by text " + filterBy)

    def clickFiltersCheckbox(self, checkboxValue):
        ckbx = self.driver.find_element('//*[@id="lot_model_desc' + checkboxValue + '"]')
        print('click on " + checkboxValue)

    def getAllFilterCheckboxes(self):
        listofcheckboxvalues = self.driver.find_element(By.XPATH, '//*[@id="//*[@id="collapseinside' + self.sectionNum +'"]//li]')
        return listofcheckboxvalues
