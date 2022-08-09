import utils


def manipulation_sheets(db, sheet, rate_us):
    """Sheet: excel data
    Updating, adding data's sheet"""
    for row in sheet[1:]:
        old_row = db.check_exists(vars=(row[0],))
        if old_row:
            if utils.compare(row, old_row, rate_us):
                continue
            # update data
            db.update(vars=tuple(row[1:]+row[:1]))
        else:
            data = utils.reformat_date(row, rate_us)
            # add new data
            db.add(vars=tuple(data))
