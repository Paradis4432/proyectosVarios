#%%

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



service = build('drive', 'v3', credentials=creds)

event = service.events().get(calendarId="primary", eventId="eventId").execute()
print(event["summary"])