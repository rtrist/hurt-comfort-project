#I used this to split each of the tumblr rags into a separate line
import csv

input_file_path = 'tumblrtags_2011_2013.csv'
output_file_path = 'tumbtag_2011_2013.csv'

def split_tags_and_write_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)  # Read the header

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(["Tag"])  # Write a header for the new file

            for row in reader:
                try:
                    tags = row[1:]  # Extract all values after the first one
                    for tag in tags:
                        writer.writerow([tag.strip()])  # Write each tag on a new line
                except IndexError as e:
                    print(f"Skipping row due to error: {e}")
                    print(f"Row content: {row}")





split_tags_and_write_csv(input_file_path, output_file_path)
