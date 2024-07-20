from jugaad_data.nse import NSELive
n = NSELive()


def market_status():
  status = n.market_status()
  data =status['marketState'][0]['marketStatus']
  return data

market_status()