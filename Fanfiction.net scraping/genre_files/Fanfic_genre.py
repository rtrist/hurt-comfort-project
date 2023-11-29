#I wanted only the genres, so I wanted only the first comma separated value. I ran this for each "era"

import csv


input_file = 'Fanfic_Genres_2014-2018.csv'
output_file = 'Fanfic_onlygenres_2014-2018.csv'

# Read the data from the input CSV file and extract the first value from each row
first_values = []

with open(input_file, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:  # Check if the row is not empty
            first_value = row[0]  # Get the first value
            first_values.append([first_value])

# Write the first values to a new CSV file
with open(output_file, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(first_values)

print(f"First values saved to {output_file}")
