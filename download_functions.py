import os
from settings import SETTINGS as S


def last_download():
    """Returns the text of last_download.txt."""
    with open("last_download.txt") as file:
        return file.read().replace("\n", "").strip()
    

def record_last_download(files):
    """Overwrites last_download.txt with the first filename in the specified list."""
    with open("last_download.txt", "w") as file:
        file.write(files[0])


def move_files(files, frm, to):
    """Moves the specified files to the specified location."""
    for file in files:
        current_path = os.path.join(frm, file)
        new_path = os.path.join(to, file)
        os.rename(current_path, new_path)


def files_exist(files, directory):
    """Returns True or False depending on whether the files exist in the directory."""
    for file in files:
        file_path = os.path.join(directory, file)

        if not os.path.exists(file_path):
            return False
        
    return True