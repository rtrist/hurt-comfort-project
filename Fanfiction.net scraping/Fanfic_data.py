#I used this code to pull the data from each fandom and pull out just the genres and dates.

import csv


input_file = 'HP_Genres.csv'


output_file = 'fanfic_data.csv'


with open(input_file, mode='r', newline='') as input_csvfile, open(output_file, mode='a', newline='') as output_csvfile:
    reader = csv.reader(input_csvfile)
    writer = csv.writer(output_csvfile)

    
    header = next(reader, None)
    if header:
        writer.writerow(header)

    for row in reader:
        new_row = []

        
        for value in row:
            if '-' in value:
                
                parts = value.split('-')
                for part in parts:
                    if '/' in part:
                        new_row.append(part.strip())  

        
        if new_row:
            writer.writerow(new_row)

