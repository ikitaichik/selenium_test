import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import warnings


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        s = Service('/usr/lib/chromium')
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        self.driver.close()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element(By.NAME, 'q')
        elem.send_keys("Who is Omer Keren?")
        elem.send_keys(Keys.RETURN)
        result = driver.find_element(By.TAG_NAME, 'h3')
        result.click()
        if "omer-keren-097820137" in driver.current_url:
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
