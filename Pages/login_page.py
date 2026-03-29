from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.USER_INPUT = (By.CSS_SELECTOR,"[data-testid='login-username']")
        self.PASS_INPUT = (By.ID, "login-password")
        self.SUBMIT_BTN = (By.XPATH,"//span[text()='Continue']")
        self.CODE_BOXES = (By.CSS_SELECTOR,"input[class='OTCInput__SlotInput-sc-otwh5g-3 jAHRcf']")
        self.CODE_SUBMIT_BTN = (By.CSS_SELECTOR,"div.Group-sc-u9bcx5-0 > button.Button-sc-qlcn5g-0 > span.ButtonInner-sc-14ud5tc-0")

    def login(self, user):
        logger.info(f"Logging in with user: {user}")
        try:
            user_field = self.wait.until(EC.visibility_of_element_located(self.USER_INPUT))
            user_field.send_keys(user)
            logger.info("Username entered")
            
            submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN))
            submit_btn.click()
            logger.info("Continue button clicked")
        except Exception as e:
            logger.error(f"Error in login: {str(e)}")
            raise

    def wait_for_manual_code_and_login(self, timeout_minutes=5):
        logger.info(f"Waiting for manual code entry (timeout: {timeout_minutes} min)")
        try:
            code_waiter = WebDriverWait(self.driver, timeout_minutes * 60)
            code_elements = code_waiter.until(EC.presence_of_all_elements_located(self.CODE_BOXES))
            logger.info(f"Found {len(code_elements)} code input boxes")
            
            code = input(f"Enter code from email (you have {timeout_minutes} min): ").strip()
            logger.info("Code received from user")

            if len(code_elements) > 1 and len(code) == len(code_elements):
                for i, digit in enumerate(code):
                    code_elements[i].send_keys(digit)
            else:
                code_elements[0].clear()
                code_elements[0].send_keys(code)

            code_submit = code_waiter.until(EC.element_to_be_clickable(self.CODE_SUBMIT_BTN))
            code_submit.click()
            logger.info("Code submitted")
        except Exception as e:
            logger.error(f"Error in code entry: {str(e)}")
            raise