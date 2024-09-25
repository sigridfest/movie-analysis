# Import necessary libraries for web scraping and CSV file manipulation
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The URL for top 250 movies
url = 'https://www.imdb.com/chart/top/'

# Initialize the Chrome WebDriver and navigate to URL
browser = webdriver.Chrome()
browser.get(url)

# XPath to the list of movies
xpath = '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li'

# Wait for all movie elements located by the XPath to be loaded on the page
WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath))
)

# Find all movie elements by their XPath
movies = browser.find_elements(By.XPATH, xpath)

# Initialize a list for movie data, including a header row
movies_data = [["Rank", "Title", "Release Year", "Duration", "Age Rating", "Rating", "Amount of Reviews"]]

# Extract data from each movie element
for movie in movies:
    details = movie.text.split('\n')
    rank_title = details[0].split('. ', 1)  # Split the rank and title
    rank = rank_title[0]  # Rank is before the dot
    title = rank_title[1]  # Title is after the dot
    release_year = details[1]  # Release year is the second line
    duration = details[2]  # Duration is the third line
    age_rating = details[3]  # Age rating is the fourth line
    rating = details[4]  # Rating is the fifth line
    amount_of_reviews = details[5].strip(' ()').replace('K', '000')  # Convert 'K' in reviews to '000'
    
    # Append the extracted data for the current movie to the list
    movies_data.append([rank, title, release_year, duration, age_rating, rating, amount_of_reviews])

# Write the extracted movie data to a CSV file
with open('imdb_top_250.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(movies_data)

# Close the browser
browser.quit()