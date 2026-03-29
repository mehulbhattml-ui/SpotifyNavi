from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import functools
import time
from selenium.webdriver.common.keys import Keys
import logging

logger = logging.getLogger(__name__)


# Retry decorator for stale elements
def retry_on_stale(retries=3):
    def outer(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            for i in range(retries):
                try:
                    return fn(*args, **kwargs)
                except StaleElementReferenceException:
                    if i == retries - 1:
                        raise
            return None
        return inner
    return outer


class SpotHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        logger.info("SpotHomePage initialized")
        
        # Locators
        self.LOGIN_ENTRY = (By.CSS_SELECTOR, "[data-testid='login-button']")
        self.SEARCH_INPUT = (By.CSS_SELECTOR, '[data-testid="search-input"]')
        self.HINDI_CARD = (By.CSS_SELECTOR, "[data-testid='herocard-click-handler']")
        self.SONG_LIST = (By.CSS_SELECTOR,'[data-encore-id="card"]:first-of-type div[role="button"][tabindex="0"]')
        self.PLAY_BTN = (By.CSS_SELECTOR, '[data-testid="action-bar"] button.e-10180-legacy-button-primary')
        self.PROFILE_MENU = (By.CSS_SELECTOR, "[data-testid='username-first-letter']")
        self.LOGOUT_BTN = (By.XPATH,"//span[text()='Log out']")
        self.PROFILE = (By.XPATH, "//span[text()='Profile']")
        self.PRO_NAME = (By.CSS_SELECTOR,"button.Ilca7f6UmkkZP2dG > span.oxLp8IMmA_4VHPP8 > h1.e-10180-text")

    def navigate_to_login(self):
        logger.info("Clicking login entry button")
        try:
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_ENTRY)).click()
            logger.info("Login entry clicked")
        except Exception as e:
            logger.error(f"Error clicking login entry: {str(e)}")
            raise

    def search_for(self, term):
        logger.info(f"Searching for: {term}")
        try:
            search = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
            search.send_keys(term)
            search.send_keys(Keys.RETURN)
            logger.info(f"Search submitted for '{term}'")
            time.sleep(10)
        except Exception as e:
            logger.error(f"Error in search_for: {str(e)}")
            raise

    @retry_on_stale(retries=3)
    def clicksearchresultandsonglist(self):
        logger.info("Clicking search result and song list")
        try:
            searchcard = self.wait.until(EC.element_to_be_clickable(self.HINDI_CARD))
            logger.info("Hindi card is visible")
            searchcard.click()
            time.sleep(10)

            songlists = self.wait.until(EC.element_to_be_clickable(self.SONG_LIST))
            logger.info("Song list is visible")
            time.sleep(10)
            songlists.click()
            logger.info("Song clicked")
        except Exception as e:
            logger.error(f"Error in clicksearchresultandsonglist: {str(e)}")
            raise

    def play_and_pause_song(self):
        logger.info("Playing and pausing song")
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.PLAY_BTN))
            btn.click()
            logger.info("Play button clicked")
            time.sleep(30)
            
            btn = self.wait.until(EC.element_to_be_clickable(self.PLAY_BTN))
            btn.click()
            logger.info("Pause button clicked")
            time.sleep(10)
        except Exception as e:
            logger.error(f"Error in play_and_pause_song: {str(e)}")
            raise

    @retry_on_stale(retries=3)
    def open_profile(self):
        logger.info("Opening profile menu")
        try:
            profile_menu = self.wait.until(EC.element_to_be_clickable(self.PROFILE_MENU))
            profile_menu.click()
            logger.info("Profile menu opened")
        except Exception as e:
            logger.error(f"Error in open_profile: {str(e)}")
            raise

    @retry_on_stale(retries=3)
    def get_profile_name(self):
        logger.info("Getting profile name")
        try:
            self.wait.until(EC.visibility_of_element_located(self.PROFILE))
            name_element = self.wait.until(EC.visibility_of_element_located(self.PRO_NAME))
            profile_name = name_element.text.strip()
            logger.info(f"Profile name retrieved: {profile_name}")
            return profile_name
        except Exception as e:
            logger.error(f"Error in get_profile_name: {str(e)}")
            raise

    def logout(self):
        logger.info("Attempting logout")
        try:
            self.wait.until(EC.element_to_be_clickable(self.PROFILE_MENU)).click()
            self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
            logger.info("Logout successful")
        except Exception as e:
            logger.warning(f"Logout failed (may already be logged out): {str(e)}")