from datetime import datetime
import requests
import xml.etree.ElementTree as ET
from config import TOKEN, chatID, logging


def reformat_date(data, rate_us):
    """Datetime change format"""
    data[3] = datetime.strptime(data[3], "%d.%m.%Y").date()
    data.append(round(int(data[2])*rate_us,2))
    return data

# todo: fix
def compare(new, old_r, rate_us):
    new = reformat_date(new, rate_us)[1:]
    new_row = []
    for i in new:
        if isinstance(i, str):
            new_row.append(int(i))
        else:
            new_row.append(i)
    for i in range(len(new)-1):
        if new_row[i] != old_r[i]:
            return False
    return True


def cbr():
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=07/08/2022"
    res = requests.get(url)
    root = ET.fromstring(res.text)
    for neighbor in root.findall(".//Value/..[@ID='R01235']"):
        result = neighbor.find('Value').text
        result = result.replace(',','.')
        return float(result)


def notification_tg(date):
    now = datetime.now().date()
    note = "Срок поставки прошел"
    if date < now:
        return
    logging.info("Send notification")
    send_text = 'https://api.telegram.org/bot' + TOKEN + \
               '/sendMessage?chat_id=' + chatID + \
               '&parse_mode=Markdown&text=' + note

    requests.get(send_text)
    # return response.json()



if __name__ == '__main__':
    date = datetime(2022,7,30).date()
    row = ['11','12497899', '617', '30.07.2022']
    old = [11, 12497899, 617, date, 64000]
    res = compare(row,old, 60)
    print(res)

