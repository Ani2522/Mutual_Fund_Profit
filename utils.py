import requests
from datetime import datetime

def getNav(date_str):
    url=f"https://api.mfapi.in/mf/101206"
    response=requests.get(url)
    navData=response.json()['data']
    Date=datetime.strptime(date_str, "%d-%m-%Y")
    for i in navData:
        j=datetime.strptime(i['date'], "%d-%m-%Y")
        if j<=Date:
            return float(i['nav'])

    lastData=navData[-1]
    return float(lastData['nav'])

def calculate_profit(scheme_code, start_date, end_date, capital=1000000.0):
    st=getNav(start_date)
    en=getNav(end_date)

    units=capital / st
    val=units * en

    np = val - capital

    return np

