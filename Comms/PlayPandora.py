
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def play_pandora(username='willcheaqui@gmail.com', password='Jamie23@marriage', playlist_name='Wicked Tinkers Station'):
    # Start a new instance of the Chrome browser
    driver = webdriver.Chrome()

    # Navigate to the Pandora login page
    driver.get("https://www.pandora.com/account/sign-in")

    # Enter the username and password
    username_field = driver.find_element_by_name("username")
    username_field.send_keys(username)
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)

    # Click the "Sign In" button
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(5)

    # Search for the playlist
    search_field = driver.find_element_by_xpath('//input[@aria-label="Search for music"]')
    search_field.send_keys(playlist_name)
    search_field.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Click on the first search result
    first_result = driver.find_element_by_xpath('//div[@data-qa="station-item"]')
    first_result.click()

    # Wait for the playlist page to load
    time.sleep(5)

    # Find the "Play" button and click it
    play_button = driver.find_element_by_class_name("PlayButton")
    play_button.click()

    # Wait for the music to start playing
    time.sleep(10)

    # Close the browser
    driver.quit()

# play_pandora()

import requests

auth ={
    "password": "secretpassword",
    "username": "email@example.com"
}

response = requests.get('https://www.pandora.com/api/', headers=auth)
print(response)
