import utils


simple_data = [['28', '12497899', '617', '30.10.2022'],
['30', '1182407', '24444', '13.05.2022']]


def manipulation_sheets(db, sheet, rate_us):
    """Sheet: excel data
    Updating, adding data's sheet"""
    for row in sheet[1:]:
        old_r = db.check_exists(vars=(row[0],))
        if old_r:
            if utils.compare(row, old_r, rate_us):
                continue
            db.update(vars=tuple(row[1:]+row[:1]))
        else:
            data = utils.reformat_date(row, rate_us)
            db.add(vars=tuple(data))
    db.close()
