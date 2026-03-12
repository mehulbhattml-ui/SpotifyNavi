Feature: Spotify Home page and song selection
As a User i will open Google and navigate to the spotify home page


Scenario: Navigate to Spotify Home page
Given I am on Google home page
When I search for "Spotify"
Then I should see the Spotify home page in the search results


Scenario: Select a song and play
Given I am on the Spotify home page
When I search for a song "XYZ"
Then I should see the song in the search results
When I click on the song "Shape of You"
Then the song should start playing
