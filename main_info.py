def main_info(session_id):
    import requests
    import json

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.ea.com',
        'Referer': 'https://www.ea.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-UT-SID': session_id,
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }




    response = requests.get('https://utas.external.s2.fut.ea.com/ut/game/fifa22/usermassinfo', headers=headers)
    response = json.loads(response.text)

    id = response['userInfo']['personaId']
    club_name = response['userInfo']['clubName']
    credits = response['userInfo']['credits']
    print(f'credits: {credits} \nclubname: {club_name} \nid: {id}')
    return credits,club_name,id
