import time
from src.spreadsheet import data_sheet
from src.sqliter import Database
from src.recast import manipulation_sheets
import schedule
from src.utils import cbr
from config import logging
from web import create_app
import threading

# initialisations
db = Database()
RATE_US = cbr()
app = create_app()


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


# Sheet task
def main():
    logging.info("Loop starting...")
    while True:
        schedule.run_pending()
        time.sleep(1)


# Flask app
def run_app():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_app)
    api_thread = threading.Thread(target=main, daemon=True)
    flask_thread.start()
    api_thread.start()