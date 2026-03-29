Feature: Spotify Automation Suite

  Background:
    Given the user is on Google Search
    And the user searches for "Spotify" and clicks the first result
    And the user logs into Spotify with valid credentials

  Scenario: Search and play a Hindi song
    When the user searches for "Hindi" in the top navigation
    And the user clicks the "Hindi" hero card
    Then the user plays the first song and then pauses it

  Scenario: Verify User Profile Name
    When the user opens the profile menu
    Then the profile name should be visible and not empty