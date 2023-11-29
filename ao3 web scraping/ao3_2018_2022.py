import requests
from bs4 import BeautifulSoup
import csv
import time  # Import the time module

# Define the base URL
base_url = "https://archiveofourown.org/tags/Hurt*s*Comfort/works?commit=Sort+and+Filter&page={}&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bdate_from%5D=2018-01-01&work_search%5Bdate_to%5D=2022-01-01&work_search%5Bexcluded_tag_names%5D=&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=kudos_count&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D="

# Create a CSV file to store the tags

with open('ao3_tags_2018_2022.csv', 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Iterate through the pages
    for page in range(1001, 5000):  
        url = base_url.format(page)
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            freeforms = soup.find_all(class_='freeforms')

            # Iterate through the "freeforms" and find "tag" within them
            for freeform in freeforms:
                tags = freeform.find_all(class_='tag')
                
                # Extract and write tags to the CSV file
                tag_list = [tag.get_text() for tag in tags]
                csv_writer.writerow(tag_list)
            
            print("Page", page, "done.")

            # Introduce a delay of 5 seconds before the next request
            time.sleep(5)
        else:
            print("Failed to fetch page", page, ". Status code:", response.status_code)

print("All tags over time have been scraped and saved to 'ao3_tags_2018_2022.csv'.")