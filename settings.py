with open(file='mdny_settings.txt') as file:
    settings_contents = file.readlines()

SETTINGS = {setting.split('===')[0]: setting.split('===')[1].replace('\n', '').strip() for
        setting in settings_contents if "===" in setting}
