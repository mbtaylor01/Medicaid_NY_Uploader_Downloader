from settings import SETTINGS as S


def last_download():
    """Returns the text of last_download.txt."""
    with open("last_download.txt") as file:
        return file.read().replace("\n", "").strip()