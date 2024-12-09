#!/usr/bin/env python3

import json

#file_path = '/home/trademachine/PFT/mistral_wAI_scores1.json'
file_path = '/home/trademachine/PFT/mistral_woAI_scores1.json'
#file_path = '/home/trademachine/PFT/gpt-4o_wAI_scores1.json'
#file_path = '/home/trademachine/PFT/gpt-4o_woAI_scores1.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)


def strings_to_dict(string_list):
    return {k.strip(): float(v.strip()) for k, v in (s.split(':', 1) for s in string_list)}

#print(strings_to_dict(json_data))
result = strings_to_dict(json_data)

def rank_json_keys_by_value(data):
    # Parse JSON if it's a string, otherwise use the dictionary directly
    #data = json.loads(json_data) if isinstance(json_data, str) else json_data
    
    # Sort the items by value in descending order
    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    
    # Extract and return only the keys
    return [item for item in sorted_items]


ranked = rank_json_keys_by_value(result)
#for each in ranked[0:30]:
    #print(f'{each[0]}:', each[1])


with open('mistral_woAI_scores1_top30.json', 'w') as f:
    json.dump(ranked[0:30], f, indent=2)

