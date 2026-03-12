import pytest
import selenium 
import webdriver_manager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver

class GoogleSearch:

    google='https://google.com'
   # googleSearchBar = (By.CSS_SELECTOR,"input[class='truncate']")
    googleSearchBar = (By.NAME,"q")
    googleSearchResult = (By.XPATH,"//h3[contains(text(),'Spotify - Web Player: Music for everyone')]")
    SpotifyLanding= (By.XPATH,"//*[contains(text(),'Spotify - Web Player: Music for everyone')]")
  #  SongPlay = By.CSS_SELECTOR,


    def __init__(self, driver):
    #Using undetected chromedriver with version 145 to avoid the CPATCHE.
        self.driver = driver
        print("driver instance is created")
        self.wait = WebDriverWait(self.driver,30)
    
    def Google_Open(self):
        self.driver.get(self.google)
        print(f"Navigate to: {self.driver.title}")
        self.wait.until(EC.visibility_of_element_located(self.googleSearchBar))
        print('Google home page is visible successfully')


    def Google_Search(self,text):
        
        search_element = self.wait.until(EC.element_to_be_clickable(self.googleSearchBar))
      #  search_element = self.driver.find_element(*self.googleSearchBar)
        search_element.click()
        search_element.send_keys(text)
      # self.wait = WebDriverWait(driver,10)
        search_element.submit()

    def Click_Search_Result(self):
        self.wait.until(EC.visibility_of_element_located(self.googleSearchResult)).click()
        print("Search Result has clicked successfully")


    def Spotify_Landing_Page(self):
        self.wait.until(EC.title_contains("Spotify - Web Player: Music for everyone"))
           


        

       
        
        


   
   
#def SelectSong(self):
#       WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SongPlay)).click()


if __name__ == "__main__":

    options =undetected_chromedriver.ChromeOptions()
    driver = undetected_chromedriver.Chrome(version_main=145,options=options)
    try:
        home_page = GoogleSearch(driver)
        home_page.Google_Open()
    
    finally:
        driver.quit()

