from datetime import datetime
import requests
import xml.etree.ElementTree as ET
from config import TOKEN, chatID


def reformat_date(data, rate_us):
    """Datetime change format"""
    data[3] = datetime.strptime(data[3], "%d.%m.%Y").date()
    # send notification
    notification_tg(data[3])
    data.append(round(int(data[2])*rate_us,2))
    return data


def compare(new_r, old_r, rate_us):
    new = reformat_date(new_r, rate_us)[1:]
    new_r = []
    for i in new:
        if isinstance(i, str):
            new_r.append(int(i))
        else:
            new_r.append(i)
    for i in range(len(new)):
        if new_r[i] != old_r[i]:
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
    if date > now:
        return
    send_text = 'https://api.telegram.org/bot' + TOKEN + \
               '/sendMessage?chat_id=' + chatID + \
               '&parse_mode=Markdown&text=' + note

    requests.get(send_text)
    # return response.json()



if __name__ == '__main__':
    res = ['11', '12497899', '617', '30.07.2022']
    reformat_date(res, 60)
    pass

