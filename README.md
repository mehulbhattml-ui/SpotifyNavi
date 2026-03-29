# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

Project Title = Spotify Navigation and Playback Automation
Description = A Python project that automates navigation and playback on Spotify using Selenium WebDriver
Author = M Bhatt
License = MIT License
Setup Instruction :-
1. Install Python 3.8 or higher.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and add it to your system PATH.
4. Run the script using:
   ```
   pytest -s SpotifyNavi\stepdefination\test_SpotifySongPlay.py
   ```
It's uses mfa as the -S disables pytes's default output capturing, allwing the terminal to prompt you for the email verfication code sent by spotify during the login process. 
Usage :-
1. The script will open a browser window and navigate to the Spotify login page.
2. Enter your Spotify credentials and complete the login process, including any multi-factor authentication if enabled.
3. Once logged in, the script will search for a specified song and play it.
4. The script will then close the browser after the song starts playing

Future improvement:-
1) The scenario two of profile validation and logout will be implemented. 
2) MFA will replace with the IMAP/Gmail API integration to remove the dependency of -s flag and comply with CI/CD.

