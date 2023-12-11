# hurt-comfort-project

Methodology

I first scrape Ao3 which can be found in the ao3 web scraping folder which was very straightforward.

Then I tried to web scrape Fanfiction.net which was more complicated. This process can be found in the Fanfiction.net folder. fanfic_intital_scrape.py is the first code, I then did the same code with different fandoms (twilight_scrape.py and naruto_scrape.py) These are the three largest fandoms on the site. 
Then I used Fanfic_data.py to try and pull just the genres and dates from those initial csvs. I wanted to sort them by date.
Then I wrote cleaning_fanfic.py where I was trying to get just the genres and dates but failed. However, this script made it so the last comma separated value was just a date, so I tried to work with this. I had some code that put the first and last value into a new file which was final_fanfic_data.csv, but I don't know where that file went sorry. Then in fanfic_genre_years.py I sorted them by that last value. 
Then I used fanfic_genre.py to sort them into files by every four years.

Then I used Tumblr's API to get every post ever tagged Hurt/comfort. I used the file Tumblr_api_test.py. It stopped running after a bit because the sleep wasn't long enough so I had to run it twice, starting the second time from the date it left off. This created files with the tag and date so I could sort them by year. Then I used organize_year.py to put them into files by year. Then I used tumblrtags_only.py to get rid of the dates. Then I used organizetags.py to put each tag on a separate line so it could match the rest of my data.

Then I put all the year files from each source together to make total tags in the total tags file.

Then I wanted to do a categorization/sentiment analysis of these tags, so I used categories.ipynb. I ran this for a sample of the total tags then averaged the percentages. 



 
