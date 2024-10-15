
from .nse_rajesh import fetch_nse_data


def market_status_1():
    api_url = "https://www.nseindia.com/api/marketStatus"
    data = fetch_nse_data(api_url)
    data = data.get('marketState')
    data = data[0]['marketStatus']
    return data


