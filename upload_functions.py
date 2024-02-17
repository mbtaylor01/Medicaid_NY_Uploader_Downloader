import os
from settings import SETTINGS as S


def files_to_upload(directory):
    """Returns the valid upload files in the specified directory."""
    valid_files = [file for file in os.scandir(directory) if valid_upload_file(file)]

    return valid_files


def valid_upload_file(file):
    """Returns true if the file is a valid upload file."""
    return file.name.startswith(S["upload_file_prefix"]) and os.path.isfile(file.path)