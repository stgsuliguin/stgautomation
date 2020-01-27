class navigateTo:
    def __init__(self,driver):
        self.driver = driver
        print "initializing navigateTo"

    def goTo(self, url, verifyText):
        self.driver.get(url)
        print ("taking screenshot w/file name " + testname)
        
