from __future__ import print_function
import pickle
import os.path
import random
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SCOPES = ['https://www.googleapis.com/auth/documents']

# TODO
DOCUMENT_ID = 'INSERT_DOC_ID_HERE'


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    title = document.get('title')
    print('The title of the document is: {}'.format(title))

    # Find & Replace
    value1 = 'I am just a text'
    value2 = 'Some randomness: {}'.format(random.randint(0, 1000))
    requests = [
        {
            'replaceAllText': {
                'containsText': {
                    'text': '{{param1}}',
                    'matchCase': 'true'
                },
                'replaceText': value1 + '\n{{param1}}',
            }
        },
        {
            'replaceAllText': {
                'containsText': {
                    'text': '{{param2}}',
                    'matchCase': 'true'
                },
                'replaceText': value2 + '\n{{param2}}'
            }
        }
    ]

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
    print(result)


if __name__ == '__main__':
    main()
