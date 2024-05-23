import os

class Settings:
    def __init__(self):
        self.file_path = "./utils/settings.conf"
        if not os.path.exists(self.file_path):
            self.create_settings_file()

    def create_settings_file(self):
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                pass
            return True
        return False

    def write_to_settings_file(self, setting, value):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r+") as file:
                lines = file.readlines()
                file.seek(0)
                found = False
                for line in lines:
                    if line.startswith(f"{setting} = "):
                        file.write(f"{setting} = {value}\n")
                        found = True
                    else:
                        file.write(line)
                if not found:
                    file.write(f"{setting} = {value}\n")
                file.truncate()
            return True
        return False

    def read_from_settings_file(self, setting):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    s, value = line.strip().split(" = ")
                    if s == setting:
                        return value
        return None