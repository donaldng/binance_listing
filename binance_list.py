import requests, time, sys, time
from client import TradeClient, Client
import config

#bfx = TradeClient(config.key,config.secret)
#execute = bfx.place_order("10", "1", "buy", "market", "iotusd")

listed = 0

while(1):
    try:
        if listed:
            sys.exit()

        url = "https://binance.zendesk.com/hc/en-us/sections/115000106672-New-Listings"
        r = requests.get(url).text

        if "binance lists iota" in r.lower() or "binance lists iot" in r.lower():
            listed = 1
            bfx = TradeClient(config.key,config.secret)
            execute = bfx.place_order("15000", "1", "buy", "market", "iotusd")
            print(execute)
            time.sleep(5)
            sys.exit()
        else:
            print("Searching... %s" % time.time())
    except:
        pass

    time.sleep(10)