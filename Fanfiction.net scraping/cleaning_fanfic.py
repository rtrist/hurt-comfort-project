#I used this code to try and clean the fanfic data to just the dates and genres but that didn't quite work. However I got it so that the last comma separated value was just a date.

import csv
import re


input_file = 'fanfic_data.csv'


output_file = 'cleaned_fanfic_data.csv'


with open(input_file, mode='r', newline='') as input_csvfile, open(output_file, mode='w', newline='') as output_csvfile:
    reader = csv.reader(input_csvfile)
    writer = csv.writer(output_csvfile)

    for row in reader:
        cleaned_row = []

        
        for value in row:
            
            genres = re.findall(r'(\w+(?:/\w+)*)', value)
            if genres:
                cleaned_row.append('/'.join(genres))

            
            publish_date = re.search(r'>([^<]+)<', value)
            if publish_date:
                cleaned_row.append(publish_date.group(1))

        
        if cleaned_row:
            writer.writerow(cleaned_row)


#So then I ran a code to find the first and last comma separated value and write that to a file:

import csv
import re


input_file = 'cleaned_fanfic_data.csv'


output_file = 'final_fanfic_data.csv'


with open(input_file, mode='r', newline='') as input_csvfile, open(output_file, mode='w', newline='') as output_csvfile:
    reader = csv.reader(input_csvfile)
    writer = csv.writer(output_csvfile)

    for row in reader:
        if len(row) >= 2:
            cleaned_row = [row[0], row[-1]]
            writer.writerow(cleaned_row)