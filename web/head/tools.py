def total(sheet):
    sum = 0
    for i in sheet:
        sum+=i['price_us']
    return sum
