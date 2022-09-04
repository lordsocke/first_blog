def buying(session_id,player,buy_price,sell_price, sell_price_low,rarity_id="1",profit="0" ):
    import requests
    import time
    import json

    headers = header(session_id)

    params = {
        'num': '21',
        'start': '0',
        'type': 'player',
        'maskedDefId': player,
        'maxb': buy_price,
        'rarityIds': rarity_id,
    }
    #searching Player at market
    response = requests.get('https://utas.external.s2.fut.ea.com/ut/game/fifa22/transfermarket', params=params, headers=headers) 
    response = json.loads(response.text)
    len_list = len(response["auctionInfo"])
    if len_list != 0:
        print(str(len_list)+" players found for price")
        trade_id = (response["auctionInfo"][(len_list-1)]['tradeId'])
        item_id = (response["auctionInfo"][(len_list-1)]['itemData']['id'])
        price = (response["auctionInfo"][(len_list-1)]['buyNowPrice'])
        
        bid(price, trade_id, headers)
        send_to_tradepile(item_id, headers)
        item_id = list_player_at_market(item_id, sell_price_low, sell_price,headers)
        item_id = item_id['idStr']
        profit = profit + ((sell_price*0.95) - price)
        print(str(profit)+" profit made")
        time.sleep(10)
    elif len_list == 0:
        #if there was no player, send message
        print('no objects at the market')
        time.sleep(15)
        item_id = 0
        #wait for X seconds before repeat
    return profit, item_id

def bid(price, trade_id, headers):
    import requests
    import json
    print("trying to buy item for "+str(price))
    # make a bid to the player (buynow)
    data = ('{"bid":%s}'%price)
    response = requests.put('https://utas.external.s2.fut.ea.com/ut/game/fifa22/trade/%s/bid'%trade_id, headers=headers, data=data)
    response = json.loads(response.text)
    return response

def send_to_tradepile(item_id, headers):
    import requests
    import json
    data = ('{"itemData":[{"id":%s,"pile":"trade"}]}'%item_id)
    #sending Item to tradepile
    response = requests.put('https://utas.external.s2.fut.ea.com/ut/game/fifa22/item', headers=headers, data=data)
    print("player send to tradepile")
    response = json.loads(response.text)
    return response

def list_player_at_market(item_id, sell_price_low, sell_price,headers):
    import requests     
    import json
    data = ('{"itemData":{"id":%s},"startingBid":%s,"duration":3600,"buyNowPrice":%s}' %(item_id, sell_price_low, sell_price))
    #listing Player at given price
    response = requests.post('https://utas.external.s2.fut.ea.com/ut/game/fifa22/auctionhouse', headers=headers, data=data)
    print("player was listed for %s"%sell_price)
    response = json.loads(response.text)
    return response

def header(session_id):
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
    return headers
