import csv

input_file_path = 'tags_2018_2022.csv'
output_file_path = 'alltags_2018_2022.csv'

def split_and_write_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)  # Read the header

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(["Split Value"])  # Write a header for the new file

            for row in reader:
                try:
                    values = row[1].split(', ')  # Split the second value by comma and space
                    for value in values:
                        writer.writerow([value.strip()])  # Write each value on a new line
                except IndexError:
                    print(f"Skipping row due to missing second value: {row}")

# Example usage


split_and_write_csv(input_file_path, output_file_path)
