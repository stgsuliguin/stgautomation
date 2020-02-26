from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import json
import requests
import unittest

class challenge9(unittest.TestCase):

#    def test_json(self):
#        url = "https://deckofcardapi.com/api/deck/new/shuffle/?deck_count=1"
#        response = requests.get(url)
#        jo = json.loads(response.text)
#        print(jo["deck_id"])
#        print(jo["success"])
#        print(jo["shuffled"])
#        print(jo["remaining"])

        json_string= """
                {
                    "researcher":   {
                        "name":  "Ford Perfect",
                        "species":  "Betelgeusian",
                        "relatives": [
                            {
                                "name":  "Zaphod Beeblebrox",
                                "species":  "Betelgeusian"
                },
                {
                        "name":  "Relative2 Beeblebrox",
                        "species":  "Betelgeusian"
                }
        ]

    }
}"""

data = json.loads(json_string)
print(data["researcher"]["name"])
print(data["researcher"]["relatives"][0]["name"])
print(data["researcher"]["relatives"][1]["name"])
