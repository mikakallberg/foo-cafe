import gspread
from google.oauth2.service_account import credentials

SCOPE [
    https://www.googleapis.com/auth/drive.file
    https://www.googleapis.com/auth/spreadsheets
]

CREDS = credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Copy of Goto10 hours(dev-version)')