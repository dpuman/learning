from email import header
import requests
import json
URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    data = {}

    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()
# get_data(1)


def post_data(id=None):
    data = {
        'name': 'Shatil',
        'roll': 107,
        'city': 'Borishal',
    }

    json_data = json.dumps(data)

    headers = {"Content-Type": "application/json; charset=utf-8"}
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


post_data()


def update_data(id=None):
    data = {
        'id': 1,
        'name': 'Dipankar',

        'city': 'Rajsahi',

    }

    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data(id=None):
    data = {
        'id': 6,

    }

    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# delete_data()
