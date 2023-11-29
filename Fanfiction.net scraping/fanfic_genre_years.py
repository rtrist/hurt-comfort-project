#So then I sorted that file by year so that I could make separate files with similar categories to my AO3 files. I wanted every 4 years because I viewed those as eras


import csv


input_file = 'final_fanfic_data.csv'
output_file = 'sorted_fanfic_data.csv'

data = []

with open(input_file, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  
    for row in csv_reader:
        data.append(row)


sorted_data = sorted(data, key=lambda row: row[-1].split('/')[-1])


with open(output_file, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)  
    csv_writer.writerows(sorted_data)

print(f"Data sorted by year and saved to {output_file}")


#I realized quite late in the process that some dates and stories seemed to be repeated and i have no idea why.