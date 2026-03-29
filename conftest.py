import pytest
import undetected_chromedriver as uc
from Pages.SpotHomePage import SpotHomePage
import time
import logging
import os
from datetime import datetime
import sys


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_run.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)






@pytest.fixture(scope="session")
def driver():
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--single-process')
    options.add_argument('--disable-setuid-sandbox')
    
    # Use eager page load strategy to reduce wait times
    prefs = {"profile.default_content_settings.popups": 0}
    options.add_experimental_option("prefs", prefs)

    max_attempts = 3
    driver = None
    last_exc = None
    for attempt in range(1, max_attempts + 1):
        try:
            logger.info(f"Attempt {attempt}/{max_attempts} to start Chrome driver...")
            # Align with local Chrome version; change to 147 if Chrome upgraded.
            driver = uc.Chrome(options=options, version_main=146)
            logger.info("Chrome driver started successfully")
            break
        except Exception as e:
            last_exc = e
            logger.warning(f"Attempt {attempt} failed: {str(e)}")
            if attempt < max_attempts:
                time.sleep(3)  # Increased from 2 to 3 seconds
            else:
                raise

    if driver is None:
        raise RuntimeError(f"Could not start Chrome driver after {max_attempts} attempts: {last_exc}")

    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.implicitly_wait(0)  # No implicit wait; use explicit waits in page objects
    logger.info("Driver timeouts and implicit wait configured")

    yield driver
    
    # Teardown: quit driver safely
    try:
        logger.info("Starting driver teardown...")
        driver.quit()
        logger.info("Driver quit successfully")
    except Exception as e:
        logger.error(f"Error while quitting driver: {str(e)}")
    

@pytest.fixture
def credentialsUser():
    return {
        "user": "wyndhamcricketclub+@gmail.com",
        
    }

@pytest.fixture
def credentialsPass():
    return{
       "pass": ""
    }
   
 # Auto-capture screenshot on test failure
@pytest.fixture(autouse=True, scope="function")
def screenshot_on_failure(request, driver):
    """Automatically capture screenshot on test failure"""
    yield
    
    # Check if test failed
    if request.node.rep_call.failed:
        try:
            # Create screenshots directory if it doesn't exist
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{screenshot_dir}/FAILED_{request.node.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
            logger.error(f"Screenshot captured on failure: {screenshot_name}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")                   
    