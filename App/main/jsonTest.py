import json

with open('data.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'])