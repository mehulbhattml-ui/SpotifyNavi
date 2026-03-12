from pytest_bdd import scenario, given, when, then
from SpotifyNavi.Pages.GoogleSearch import GoogleSearch
import os

# Get the directory where THIS script is located
base_path = os.path.dirname(__file__)
# Go up one level to SpotifyNavi, then into features
feature_file = os.path.join(base_path, "..", "features", "SpotifySongPlay.feature")



@scenario(r'../features\SpotifySongPlay.feature', 'Navigate to Spotify Home page')
def test_navigate_to_spotify_home_page():
    """Navigate to Spotify Home page."""
    pass


@scenario(r'../features\SpotifySongPlay.feature', 'Select a song and play')
def test_select_a_song_and_play():
    """Select a song and play."""
    pass

@given('I am on Google home page')
def Navigate_to_google(context):
    """I am on Google home page."""
    context.google = GoogleSearch(context.driver)
    context.google.Google_Open()
   
@when('I search for "Spotify"')
def Search_Spotify(context):
    """I search for "Spotify"."""
    context.google.Google_Search("Spotify")

@then('I should see the Spotify home page in the search results')
def Google_Search_for_Spotify(context):
    """I should see the Spotify home page in the search results."""
    context.google.Click_Search_Result()

@given('I am on the Spotify home page')
def Search_Open_Spotify(context):
    """I am on the Spotify home page."""
    Expected_Title = "Spotify - Web Player: Music for everyone"
    try:
       context.google.Spotify_Landing_Page()
    except:
        TitleVisible = context.driver.title
        print(f"Expected title: {Expected_Title}, but got: {TitleVisible}")

@when('I search for a song "XYZ"')
def _():
    """I click on the song "XYZ"."""
    raise NotImplementedError


@then('I should see the song in the search results')
def _():
    """I should see the song in the search results."""
    raise NotImplementedError


@when('I click on the song "Shape of You"')
def _():
    """I search for a song "Shape of You"."""
    raise NotImplementedError



@then('the song should start playing')
def _():
    """the song should start playing."""
    raise NotImplementedError