from time import time
from search_transfermarket import *
from buy import *
from main_info import *
import time

session_id = '2ed5f314-94e9-404c-9753-b1854a2e9c51'
session_id_slave = '2ed5f314-94e9-404c-9753-b1854a2e9c51'
player_id = '216201' #williams
rarity_id = "1"
min_buy_price = 0
max_buy_price = 5000
trade_id = 346529348537
profit = 0

#get main Info of account
main_info(session_id=session_id)

# set prices for player 
auctions = search_all_transfermarkt(session_id=session_id,player_id=player_id,min_buy_price=min_buy_price,max_buy_price=max_buy_price,rarity_id=rarity_id)
min_price = get_min_price(auctions=auctions)
buy_price, sell_price_low, sell_price = min_price_set(min_price=min_price)
print(buy_price, sell_price_low, sell_price)

sell_price_low = sell_price_low *2
sell_price = sell_price*2
#loop buying players at the market
for i in range(400): 
    profit,trade_id = buying(session_id=session_id,player=player_id,buy_price=buy_price,sell_price=sell_price,sell_price_low=sell_price_low,rarity_id=rarity_id, profit=profit)
    print(trade_id)
    if trade_id != 0:
        headers = header(session_id_slave)
        price = sell_price
        print(bid(price, trade_id, headers))
        print(send_to_tradepile(trade_id, headers))
        print("mule sucessfull transfered")
        time.sleep(30)