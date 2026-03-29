from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import conftest
import time



logger = logging.getLogger(__name__)

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.SEARCH_BOX = (By.NAME, "q")
        self.SPOTIFY_LINK = (By.PARTIAL_LINK_TEXT, "Spotify - Web Player")

    def navigate(self):
        logger.info("Navigating to Google")
        self.driver.get("https://www.google.com")
        time.sleep(2)

    def search_spotify(self, text):
        logger.info(f"Searching for '{text}'")
        try:
            search_el = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
            search_el.clear()
            search_el.send_keys(text + Keys.ENTER)
            logger.info("Search submitted")

            spotify_link = self.wait.until(EC.element_to_be_clickable(self.SPOTIFY_LINK))
            spotify_link.click()
            logger.info("Spotify link clicked")
            time.sleep(3)
        except Exception as e:
            logger.error(f"Error in search_spotify: {str(e)}")
            raise