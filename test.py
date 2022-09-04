import requests
import json
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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-UT-SID': '2ed5f314-94e9-404c-9753-b1854a2e9c51',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'num': '21',
    'start': '0',
    'type': 'player',
    'maskedDefId': '150418',
}

response = requests.get('https://utas.external.s2.fut.ea.com/ut/game/fifa22/transfermarket', params=params, headers=headers)
response = json.loads(response.text)
for i in range(len(response['auctionInfo'])):
    print(response['auctionInfo'][i-1]['sellerName'])
print("done")