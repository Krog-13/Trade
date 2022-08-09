import time
from spreadsheet import data_sheet
from sqliter import Database
from recast import manipulation_sheets
import schedule
from utils import cbr
from config import logging

# initialisations
db = Database()
RATE_US = cbr()


# us to rus exchange rate
def rate():
    global RATE_US
    try:
        RATE_US = cbr()
    except ConnectionError:
        pass


def start():
    """Main scheduling"""
    logging.info('Start')
    new_date = data_sheet()
    try:
        manipulation_sheets(db, new_date, RATE_US)
    except LookupError as e:
        logging.warning(e)
    logging.info('Complete')


# Task scheduling
schedule.every().day.at("00:00").do(rate)
schedule.every(1).minutes.do(start)


def main():
    logging.info("Loop starting...")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()