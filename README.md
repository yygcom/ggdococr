# gdoc_orc


##Python Quickstart
----
Complete the steps described in the rest of this page, and in about five minutes you'll have a simple Python command-line application that makes requests to the Drive API.

###Prerequisites
----
To run this quickstart, you'll need:

* Python 2.6 or greater.
* The pip package management tool.
* A Google account with Google Drive enabled.

##Step 1: Turn on the Drive API
----
Click this button to create a new console project and automatically enable the Drive API:

[ENABLE THE DRIVE API](https://developers.google.com/drive/api/v3/quickstart/python)

This opens a new dialog. In the dialog, do the following:

* a Select + Create a new project.
* b Download the configuration file.
* c Move the downloaded file to your working directory and ensure it is named credentials.json.

##Step 2: Install the Google Client Library
----
Run the following command to install the library using pip:
```shell
pip install --upgrade google-api-python-client oauth2client
```
See the library's [installation](https://developers.google.com/api-client-library/python/start/installation) page for the alternative installation options.
