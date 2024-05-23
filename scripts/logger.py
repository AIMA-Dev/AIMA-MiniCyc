import csv
import os
import datetime

def write_to_csv(path, values):
    """
    Writes the given values to a CSV file located at the specified path.
    
    If the file does not exist, it creates a new file and writes the header 'Value' as the first row.
    If the file already exists, it appends the values as new rows.
    
    Args:
        path (str): The path to the CSV file.
        values (list): A list of values to be written to the CSV file.
    """
    if not os.path.exists(path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Value'])

    with open(path, 'a', newline='') as file:
        writer = csv.writer(file)
        for value in values:
            writer.writerow([value])


def create_file_with_date(path):
    """
    Creates a new file with the current date as the file name in the specified path.
    If a file with the same name already exists, it appends a count number to the file name.

    Args:
        path (str): The path where the file should be created.

    Returns:
        None
    """
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{date}.csv"
    file_path = os.path.join(path, file_name)

    count = 1
    while os.path.exists(file_path):
        count += 1
        file_name = f"{date}_{count}.csv"
        file_path = os.path.join(path, file_name)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Value'])