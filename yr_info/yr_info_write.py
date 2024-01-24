from sp_li.sp import *
import csv
def yr_info_write():
    speak("What is your name?")
    name=input("Enter your name below.\n>>>")
    speak("What is your Age?")
    age=input("Enter your age below.\n>>>")
    speak("What is your Gender")
    sex=input("Enter your sex below.\n>>>")
    
    # Example data to be written to the CSV file
    data = [
        ["Name", "Age", "City"],
        [name, age, sex],
    ]

    # Specify the file path
    csv_file_path = "data.csv"

    # Write data to the CSV file
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header
        writer.writerow(data[0])

        # Write the remaining rows
        writer.writerows(data[1:])

    print(f"Thank You for providing us data!")
