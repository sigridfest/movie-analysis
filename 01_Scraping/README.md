# Contents

This module contains the functionality and output of webscraping in the project. It contains: 

 - datasci/exp folder: Contains the scripts scraping the top 250 movies on IMDb (movie_scraper) and their repective details (Movie_detail_info_scrape.ipynb), the top 100 celebs (celeb_scraper) and the reviews fo the movie "Home Alone" (ha_scraper).
 - imdb_top_250.csv: containing the data from the top 250 movies
 - imdb_top_100_celebs.csv: containing the data from the top 100 celebs
 - home_alone_reviews_enhanced.csv: containing the data from the Home Alone reviews
 - Top250_detailed_info.csv: containing the details from the 250 top movies
 - Movie_n_Celebrity.csv: containing movie and celebrity data
 - this README.me
 - .gitignore

# Package dependencies

 - Python csv package
 - Python re package
 - Python time package
 - selenium
 - pandas


# How to run
Before you run the code, it can be beneficial to have set up a virtual environment. Navigate to your project directory, then run the following commands:

For windows: 

 - pip install virtualenv 

 - virtualenv venv

 - .\venv\Scripts\activate

For macOS: 

 - python3 -m venv venv

 - python -m venv venv

 - source venv/bin/activate


After you have activated your virtual environment, you can start running the code. Navigate into the directory and execute each script seperately. 

 - To scrape top 250 movies: run movie_scraper.py through your IDE or using: python movie_scraper.py in the terminal

 - To scrape top 100 celebs: run celeb_scraper.py through your IDE or using: python celeb_scraper.py in the terminal

 - To scrape reviews of "Home Alone": run ha_scraper.py through your IDE or using: python ha_scraper.py in the terminal
   
 - Movie_detail_info_scraper.ipynb runs as a Jupyter notebook

The csv files will show up in the root folder. 
