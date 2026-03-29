import time
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.support import expected_conditions as EC
from Pages.GoogleSearch import GoogleSearchPage
from Pages.login_page import LoginPage
from Pages.SpotHomePage import SpotHomePage

scenarios('../features/SpotifySongPlay.feature')

@given("the user is on Google Search")
def open_google(driver):
    GoogleSearchPage(driver).navigate()

@given('the user searches for "Spotify" and clicks the first result')
def search_spotify(driver):
    GoogleSearchPage(driver).search_spotify("Spotify")

@given("the user logs into Spotify with valid credentials")
def login_user(driver, credentialsUser):
    home = SpotHomePage(driver)
    # Check if we need to click login (Background runs for every scenario)
    if driver.find_elements(*home.LOGIN_ENTRY):
        home.navigate_to_login()
        Lpinstance= LoginPage(driver)
        Lpinstance.login(credentialsUser["user"])
        Lpinstance.wait_for_manual_code_and_login(timeout_minutes=5)
        time.sleep(10)
       

@when('the user searches for "Hindi" in the top navigation')
def search_hindi(driver):
    SpotHomePage(driver).search_for("Hindi")

@when('the user clicks the "Hindi" hero card')
def click_card(driver):
    home = SpotHomePage(driver)
    home.clicksearchresultandsonglist()

@then("the user plays the first song and then pauses it")
def play_pause(driver):
    home = SpotHomePage(driver)
    home.play_and_pause_song()

@when("the user opens the profile menu")
def open_profile(driver):
    home = SpotHomePage(driver)
    home.open_profile()

@then("the profile name should be visible and not empty")
def verify_profile(driver):
    home = SpotHomePage(driver)
    actual_name = home.get_profile_name()
    expected_name ='Wyndham'
    assert actual_name == expected_name, f"Expected profile name to contain '{expected_name}', but got '{actual_name}'"

    


    

    