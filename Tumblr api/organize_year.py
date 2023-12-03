#I used this to organize the file tumblr_tags.csv into new files by year. I repeated this code with different dates and file paths

import csv

input_file = "tumblr_tags.csv"  
output_file = "tumblrdata_2011_2013.csv"  

def filter_and_write_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)  

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(header)  

            for row in reader:
                try:
                    date = row[0].split()[0]  
                    year = int(date.split('-')[0])  

                   
                    if 2011 <= year <= 2013:
                        writer.writerow(row)
                except (ValueError, IndexError):
                    print(f"Skipping row due to unexpected date format: {row}")

filter_and_write_csv(input_file, output_file)

