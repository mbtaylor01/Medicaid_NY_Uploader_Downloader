from settings import SETTINGS as S


def last_download():
    """Returns the text of last_download.txt."""
    with open("last_download.txt") as file:
        return file.read().replace("\n", "").strip()
    

def record_last_download(files):
    """Overwrites last_download.txt with the first filename in the specified list."""
    with open("last_download.txt", "w") as file:
        file.write(files[0])