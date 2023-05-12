import csv

# Open the original file with the data
csv_file = open('company.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file)

# Set to store unique records
unique_records = set()

# Loop to check for duplicate records and add unique records to the set
for row in csv_reader:
    # Convert the row into a tuple for easier comparison
    record = tuple(row)
    unique_records.add(record)

# Close the original file
csv_file.close()

# Open the new file to write the unique records
csv_file_unique = open('unique-company.csv', 'w', newline='', encoding='utf-8')
csv_writer_unique = csv.writer(csv_file_unique)

# Write the unique records to the new CSV file
for record in unique_records:
    csv_writer_unique.writerow(record)

# Close the new file
csv_file_unique.close()
