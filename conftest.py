import pytest
import undetected_chromedriver as uc

# We create a simple class to act as a container for our data
class TestContext:
    def __init__(self):
        self.driver = None
        self.google = None

@pytest.fixture
def context():
    """This creates the 'context' object used in your step definitions."""
    # 1. Setup the stealth driver
    options = uc.ChromeOptions()
    driver = uc.Chrome(version_main=145, options=options)
    
    # 2. Initialize our context container
    ctx = TestContext()
    ctx.driver = driver
    
    yield ctx # This sends 'context' to the test steps
    
    # 3. Cleanup after the test is done
    driver.quit()