from src import utils
from config import logging


def manipulation_sheets(db, sheet, rate_us):
    """Sheet: excel data
    Updating, adding data's sheet"""
    count = [0,0]
    for row in sheet[1:]:
        old_row = db.check_exists(vars=(row[0],))
        if old_row:
            if utils.compare(row, old_row, rate_us):
                continue
            # update data
            count[0]+=1
            db.update(vars=tuple(row[1:]+row[:1]))
        else:
            data = utils.reformat_date(row, rate_us)
            # send notification
            utils.notification_tg(row[3])
            # add new data
            count[1]+=1
            db.add(vars=tuple(data))

    logging.warning(f"Count updated - {count[0]} added - {count[1]}")