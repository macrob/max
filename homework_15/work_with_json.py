import json


data = {
  'first_name': 'Sergii',
  'last_name': 'Iepishkin',
  'sons': [
    'Max Iepishkin',
    'Timur Linskiy'
  ]
}

# to_string = json.dumps(data, indent=4)
# print(to_string)

json_string = '{"test": 5.5}'
json_data = json.loads(json_string, parse_float=str)
print(json_data)

