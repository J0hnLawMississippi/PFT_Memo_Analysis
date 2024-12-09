#!/usr/bin/env python3

import json

file_path = '/home/trademachine/PFT/full_memo_data0.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)


users = [each['user'] for each in json_data]
user_set = list(set(users))

print(user_set, len(user_set))
