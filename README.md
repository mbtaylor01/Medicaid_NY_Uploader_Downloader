# ↕️ Medicaid of NY Uploader/Downloader

Medicaid of NY is one of the few Medicaids that does not have an SFTP option to upload claim batches and download reports - someone has to log into their website and do it manually.  

Using Selenium with Chrome, this script automates the login process and will automatically upload files beginning with the characters you specify in the mdny_settings.txt file.

Any errors are reported with the Yagmail library linked to a Gmail account.

## ⚙️ mdny_settings.txt

The settings below must be followed by a triple equals sign in a mdny_settings.txt file (text in parenthesis is only an explanation of the setting; do not use parenthesis):

* driver_path===(path to the chromedriver Selenium will use)
* login_url===(where to log in to Medicaid of NY's website)
* link_timeout_seconds===(how long to wait for an element in the DOM before timing out)
* browser_is_headless===(boolean; run in the background or not)
* username===(Medicaid of NY username)
* password===(Medicaid of NY password)
* email_sender===(email address of the Gmail that reports errors)
* email_password===(app password for the Gmail)
* recipients===(email addresses to send warnings to; use format ("test@gmail.com", "test2@gmail.com", "banana@yahoo.com"))
* upload_location===(path where to the files to upload are found)
* upload_file_prefix===(the files to upload start with this)
* login_fail_subject===(subject of the warning email sent if logging in fails)
* login_fail_message===(message of the warning email)
* upload_fail_subject===(subject of the warning email sent if uploading fails)
* upload_fail_message===(message of the warning email)
* download_fail_subject===(subject of the warning email sent if downloading fails)
* download_fail_message===(message of the warning email)
* main_fail_subject===(subject of the warning email sent if an unforseen error arises)
* browser_downloads_location===(where the browser downloads files)
* final_downloads_location===(where to move the downloaded files)

## 🚨 Important! 🚨 Chromedriver Must Match Browser Version!

Selenium uses a Chromedriver program to control Google Chrome.  The Chromedriver must match the version of the browser.  

Chromedriver versions can be found here:  https://googlechromelabs.github.io/chrome-for-testing/
