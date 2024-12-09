#!/usr/bin/env python3

import json

file_path = '/home/trademachine/PFT/full_memo_data1.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

user_list = [each['user'] for each in json_data]
users = list(set(user_list))


filtered_data = list(map(lambda x: [item for item in json_data if item['user'] == x], users))

for each in filtered_data[0:10]:
    print(each[0:20])
