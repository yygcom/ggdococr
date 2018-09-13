#-*- coding:utf-8 -*-
from __future__ import print_function
import httplib2
import os
import io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    flagsx = argparse.ArgumentParser(parents=[tools.argparser])
    flagsx.add_argument("--input","-i",help="input imgfile type png, jpg, bmp, gif, pdf")
    flags = flagsx.parse_args()
    #print (os.path.dirname(flags.input))
except ImportError:
    flags = None

if not flags.input:
    print(u'请输入图片文件')
    os._exit(0)


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = os.path.join(os.path.dirname(__file__), 'drive-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(os.path.join(os.path.dirname(__file__), CLIENT_SECRET_FILE), SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    imgfile = flags.input  # Image with texts (png, jpg, bmp, gif, pdf)
    txtfile = flags.input+'.output.txt'  # Text file outputted by OCR

    mime = 'application/vnd.google-apps.document'
    res = service.files().create(
        body={
            'name': imgfile,
            'mimeType': mime
        },
        media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
    ).execute()

    downloader = MediaIoBaseDownload(
        io.FileIO(txtfile, 'wb'),
        service.files().export_media(fileId=res['id'], mimeType="text/plain")
    )
    done = False
    while done is False:
        status, done = downloader.next_chunk()

    service.files().delete(fileId=res['id']).execute()
    print("Done.")


if __name__ == '__main__':
    main()
