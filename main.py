import time
from spreadsheet import data_sheet
from sqliter import Database
from recast import manipulation_sheets
import schedule
from utils import cbr

# initialisations
db = Database()
RATE_US = cbr()


# us to rus exchange rate
def rate():
    global RATE_US
    RATE_US = cbr()


def start():
    """Main scheduling"""
    new_date = data_sheet()
    manipulation_sheets(db, new_date, RATE_US)


# Task scheduling
schedule.every().day.at("00:00").do(rate)
schedule.every(10).minutes.do(start)


def main():
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    start()