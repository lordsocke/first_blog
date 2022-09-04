from search_transfermarket import *
from buy import *
from main_info import *

session_id = 'e31928a1-28e2-4a9f-9f5c-270d614928c9'
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

#loop buying players at the market
for i in range(400): 
    profit,trade_id = buying(session_id=session_id,player=player_id,buy_price=buy_price,sell_price=sell_price,sell_price_low=sell_price_low,rarity_id=rarity_id, profit=profit)


