import csv
import os
import datetime

path = './logs/'
header = ['Title1', 'Title2', 'Title3']

def log_values(values, max_size_mb):
    directory = create_folder()
    if check_file_size(directory, max_size_mb):
        file_path = add_csv_file(directory)
    else:
        latest_file = get_latest_file(directory)
        file_path = os.path.join(directory, latest_file)
    
    write_values(file_path, values)

def create_folder():
    today = datetime.date.today()
    folder_name = today.strftime("%Y-%m-%d")
    folder_path = os.path.join(path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def add_csv_file(directory):
    file_name = "1"
    file_path = os.path.join(directory, file_name + ".csv")
    count = 1
    
    while os.path.exists(file_path):
        count += 1
        file_name = str(count)
        file_path = os.path.join(directory, file_name + ".csv")
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
    return file_path

def write_values(file_path, values):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(values)

def check_file_size(directory, max_size_mb):
    if not os.listdir(directory):
        return True
    
    latest_file = get_latest_file(directory)
    file_path = os.path.join(directory, latest_file)
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
    
    return file_size_mb > max_size_mb

def get_latest_file(directory):
    files = os.listdir(directory)
    if not files:
        return None
    latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(directory, x)))
    return latest_file
