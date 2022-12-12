import json
import pandas as pd
import re

with open('data_flat_list.json') as f:
    data = json.load(f)

general_keys = set()

for flat in data:
    general_keys |= set(map(lambda li: li.split(':')[0], flat['flat']))
    general_keys |= set(map(lambda li: li.split(':')[0], flat['building']))

columns = list(general_keys)
columns.append('position')
columns.append('price')
df = pd.DataFrame(columns=columns)

for flat in data:
    flat_data = dict(map(lambda item: (item, None), columns))
    for item in flat["flat"]:
        key, value = item.split(':')
        flat_data[key] = value
    for item in flat["building"]:
        key, value = item.split(':')
        flat_data[key] = value

    flat_data['price'] = flat['price'][0]
    min_distance = 1000000
    for item in flat['position']:
        list_distance = re.findall(r'\d+', item)
        if list_distance:
            min_d = min(map(int, list_distance))
            min_distance = min(min_distance, min_d)
    flat_data['position'] = min_distance
    
    df = df.append(flat_data, ignore_index=True)

df.to_csv('raw_data.csv')