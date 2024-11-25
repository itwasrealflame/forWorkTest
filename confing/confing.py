import json
import random
import string

CONFING_NAME = '../confing/confing.json'


def json_read():
    with open(CONFING_NAME, 'r') as jsonFile:
        data = json.load(jsonFile)
    return data


def extraxt_values(data):
    keys = ['name', 'surname', 'patronymic','telephone', 'email']
    lst = [data[key] for key in keys if key in data]
    return lst

def password_random_input():
    all_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(all_characters) for _ in range(10))
    return random_string





