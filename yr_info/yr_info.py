import csv
# Read data from a CSV file
def yr_info():
    csv_file_path = "data.csv"
    with open(csv_file_path, newline="") as csv_file:
        reader = csv.reader(csv_file)    
        # Skip the header row if it exists
        header = next(reader, None)
        # Process each row of data
        for row in reader:
            # Access individual columns if needed
            name, age, sex = row
            return name, age, sex
