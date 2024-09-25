# Import necessary libraries for web scraping and handling CSV files
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The URL of the celeb sitet
url = 'https://www.imdb.com/chart/starmeter/?ref_=nv_cel_m' 

# Initialize the Chrome WebDriver and navigate to the url
browser = webdriver.Chrome()
browser.get(url)

# XPath for the list of celebs
xpath = '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li' 

# Wait until all elements located by the XPath are present on the page
WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath))
)

# Find all celebs by their XPath
celebs = browser.find_elements(By.XPATH, xpath)

# Initialize a list to store data with a header row
celebs_data = [["Rank", "Name", "Role(s)", "Example Movie"]]

# Loop through each celebrity element to extract information
for celeb in celebs:
    # Split the text of the element by new lines to separate the pieces of data
    text_lines = celeb.text.split('\n')
    # Ensure the element contains all necessary information
    if len(text_lines) >= 4: 
        rank = text_lines[0].split(' ')[0]  # Extract the rank, which is before the first space
        name = text_lines[3]  # The name is on the fourth line
        roles = ', '.join(text_lines[4:-1])  # Join roles (could be multiple lines) into a single string
        example_movie = text_lines[-1]  # The last line contains an example movie
        
        # Append the extracted data for the current celebrity to the list
        celebs_data.append([rank, name, roles, example_movie])

# Write the extracted data to a CSV file
with open('imdb_top_100_celebs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(celebs_data)

# Close the browser
browser.quit()