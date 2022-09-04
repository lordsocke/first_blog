import requests
import json

params = {
    'pagination': '1',
    'order_by': 'top',
}

response = requests.get('https://www.futbin.com/22/comments/8/100258058', params=params)
print(response.text)
response = json.loads(response.text)

print("done")
