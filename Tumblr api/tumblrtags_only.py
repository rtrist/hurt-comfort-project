#I used this script to take only the tags and put them in a file
import csv

input_file = "tumblrdata_2018_2022.csv"  
output_file = "tumblrtags_2018_2022.csv"  

def extract_second_value(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)  # Read the header

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(["Second Value"])  # Write a header for the new file

            for row in reader:
                try:
                    second_value = row[1].strip()  # Extract the second value and remove leading/trailing whitespaces
                    writer.writerow([second_value])
                except IndexError:
                    print(f"Skipping row due to missing second value: {row}")

# Example usage

extract_second_value(input_file, output_file)