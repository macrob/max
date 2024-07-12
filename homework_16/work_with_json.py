import config
import json

data = {
  'age': 37,
  'name': 'John',
}


def write_json(data, filename):
    with open(config.PTH_PROJECT + filename, mode='w', encoding='utf8') as file:
        json.dump(data, file, indent=4)
        


write_json(data, '/data2.json')