
def search_all_transfermarkt(session_id,player_id,min_buy_price="0",max_buy_price="15000000",rarity_id= "1"):
    import requests
    import json
    import time

    start_search = 0 
    auctions = []
    num = 21

    headers = {
            'Accept': '*/*',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.ea.com',
            'Referer': 'https://www.ea.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'X-UT-SID': session_id,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

    params = {
            'num': num,
            'start': start_search,
            'type': 'player',
            'maskedDefId': player_id,
            'minb': min_buy_price,
            'maxb': max_buy_price,
            'rarityIds': rarity_id,
        }
        #searching Player at market
    response = requests.get('https://utas.external.s2.fut.ea.com/ut/game/fifa22/transfermarket', params=params, headers=headers)
    data = json.loads(response.text)

    ### Hier muss evt. noch geblättert werden!!! ###

    auctions_count = len(data["auctionInfo"])

    if auctions_count != 0:
        for i in range(auctions_count):
            auctions.append(data['auctionInfo'][i])

    while auctions_count == num:
        time.sleep(2)
        start_search = start_search + auctions_count
        print(f"start search: {start_search}")
        params = {
            'num': num,
            'start': start_search,
            'type': 'player',
            'maskedDefId': player_id,
            'minb': min_buy_price,
            'maxb': max_buy_price,
            'rarityIds': rarity_id,
        }
        #searching Player at market
        response = requests.get('https://utas.external.s2.fut.ea.com/ut/game/fifa22/transfermarket', params=params, headers=headers)
        data = json.loads(response.text)
        auctions_count = len(data["auctionInfo"])
        for i in range(auctions_count):
            auctions.append(data['auctionInfo'][i])
    return auctions

def get_min_price(auctions):
    print(str(len(auctions))+" auctions where found")
    prices = []
    for i in range(len(auctions)):
        prices.append(auctions[int(i)]['buyNowPrice'])
    min_price = (min(prices))
    prices.remove(min_price)
    min_price1 = (min(prices))
    prices.remove(min_price1)

    if (min_price / min_price1) < 0.9:
        min_price = min_price1

    print("min price found "+str(min_price))
    return min_price



def roundup_1000(x):
    import math
    return int(math.ceil(x / 50.0)) * 50

def roundup_10000(x):
    import math
    return int(math.ceil(x / 100.0)) * 100

def roundup_50000(x):
    import math
    return int(math.ceil(x / 250.0)) * 250

def roundup_100000(x):
    import math
    return int(math.ceil(x / 500.0)) * 500


def min_price_set(min_price):
    buy_price = min_price * 0.85
    if min_price < 1000:
        buy_price = roundup_1000(buy_price)
        sell_price_low = min_price - 100
        sell_price = min_price - 50
    if min_price > 1000 and (min_price < 10000):
        buy_price = roundup_10000(buy_price)
        sell_price_low = min_price - 200
        sell_price = min_price - 100
    if (min_price > 10000) and (min_price < 50000):
        buy_price = roundup_50000(buy_price)
        sell_price_low = min_price - 500
        sell_price = min_price - 250
    if (min_price > 50000) and (min_price < 100000):
        buy_price = roundup_100000(buy_price)
        sell_price_low = min_price - 1000
        sell_price = min_price - 500
    return buy_price, sell_price_low, sell_price

