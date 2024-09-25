# Import necessary libraries
import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# IMDb URL for the movie reviews
url = 'https://www.imdb.com/title/tt0099785/reviews?ref_=tt_urv'

# Initialize Chrome WebDriver and navigate to URL
browser = webdriver.Chrome()
browser.get(url)

# XPath for the "Load More" button on the IMDb reviews page
load_more_button_xpath = '//*[@id="load-more-trigger"]'

# Function to click the "Load More" button
def click_load_more_button(browser):
    try:
        # Wait for the button to be present and clickable, then click it
        load_more_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, load_more_button_xpath))
        )
        if load_more_button:
            browser.execute_script("arguments[0].click();", load_more_button)
            return True
    except Exception as e:
        print("Error clicking 'Load More':", e)
    return False

# Function to load more reviews by clicking the "Load More" button multiple times
def load_more_reviews(browser, attempts=5):
    for _ in range(attempts):
        if not click_load_more_button(browser):
            break  
        time.sleep(2)  # Wait for the page to load more reviews

# Load more reviews on the page
load_more_reviews(browser)

# XPath to locate all reviews
xpath_reviews = '//*[@id="main"]/section/div[2]/div[2]/div'
WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_reviews))
)

# Find all reviews by the XPath
reviews = browser.find_elements(By.XPATH, xpath_reviews)

# Prepare the data list with headers
reviews_data = [["Rating", "Title", "Username", "Date", "Review"]]

# Regular expression to match the date format in reviews
date_pattern = re.compile(r'\d{1,2}\s\w+\s\d{4}')

# Extract data from each review
for review in reviews:
    text = review.text
    # Skip reviews with spoilers or when no more load button is found
    if "Warning: Spoilers" in text or "No more 'Load More' button found" in text:
        continue

    # Remove default vote text
    text = re.sub(r'\d+ out of \d+ found this helpful. Was this review helpful\? Sign in to vote. Permalink', '', text, flags=re.IGNORECASE)

    # Split the review text into parts for extraction
    parts = text.split('\n')
    # Extract rating, or set to "no rating" if not present
    rating = parts[0].split('/')[0] if '/' in parts[0] else "no rating"
    # Extract the date of the review
    date_match = date_pattern.search(text)
    date = date_match.group() if date_match else "Date unknown"
    # Determine the index for title based on rating presence
    title_index = 1 if rating != "no rating" else 0
    title = parts[title_index]
    # Extract username, assuming it's the first word after the title
    username = parts[title_index + 1].split(' ')[0]
    # Combine the remaining parts as the review text
    review_text = ' '.join(parts[title_index + 2:])

    # Append the extracted data to the reviews data list
    reviews_data.append([rating, title, username, date, review_text])

# Write the reviews data to a CSV file
with open('home_alone_reviews_enhanced.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(reviews_data)

# Close the browser
browser.quit()