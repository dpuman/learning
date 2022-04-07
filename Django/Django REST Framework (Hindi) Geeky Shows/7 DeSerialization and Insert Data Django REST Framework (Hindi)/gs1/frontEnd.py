import requests
import json
URL = 'http://127.0.0.1:8000/stucreate/'

data = {

    'name': 'simran',
    'roll': 104,
    'city': 'London',
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
