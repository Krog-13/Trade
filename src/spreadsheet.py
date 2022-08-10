from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import *


def data_sheet():
    logging.info("Start reading from google sheets")
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=credentials)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    majorDimension="ROWS").execute()
        return result.get('values', [])
    except HttpError as err:
        logging.info(err)



if __name__ == '__main__':
    data_sheet()