from os import environ, path
from dotenv import load_dotenv
# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credential.json'
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '12XUt8fPdoWSCGbsDBaeTnurMZPFB_0Ju_GH_D4Lk13k'
SAMPLE_RANGE_NAME = 'A1:D'
TOKEN = environ.get('TOKEN')
# chatID = '838019137'
chatID = '1777396859'


# Database config
DATABASE_HOST = environ.get('DATABASE_HOST')
DATABASE_USERNAME = environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')
DATABASE_PORT = environ.get('DATABASE_PORT')
DATABASE_NAME = environ.get('DATABASE_NAME')
