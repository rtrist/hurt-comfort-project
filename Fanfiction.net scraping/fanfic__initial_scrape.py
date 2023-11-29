import cloudscraper
import csv
from bs4 import BeautifulSoup
import random
import time


url = "https://www.fanfiction.net/book/Harry-Potter/?&srt=4&g1=20&r=10&p={}"

with open('HP_Genres.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)


    for page in range(1, 2354):
      url = url.format(page)
      scraper = cloudscraper.create_scraper(interpreter='nodejs', delay=10, browser={'browser': 'firefox','platform': 'windows','mobile': False})
      response = scraper.get(url)

      if response.status_code == 200:
          soup = BeautifulSoup(response.text, 'html.parser')
          genre_elements = soup.find_all('div', {'class': 'z-padtop2 xgray'})
          for genre_item in genre_elements:
              csv_writer.writerow(genre_item)
          print(len(genre_elements))
          print("Page", page, "done.")
          random_number = round(random.uniform(5, 10))
          print(f"sleeping for {random_number} seconds")
          time.sleep(random_number)

      else:
          print("Failed to fetch page", page, ". Status code:", response.status_code)

    print("All genres have been scraped and saved to 'HP_Genres.csv'.")



    #I ran this code for Harry Potter, Naruto and Twilight. I just switched the URL and the file
