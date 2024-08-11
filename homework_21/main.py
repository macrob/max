from pprint import pprint
from uuid import uuid4
import certifi

from pymongo.mongo_client import MongoClient

USERNAME = 'mixer'
PASSWORD = 'wJw1BsSde0Lf7dDf'

uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@myfirstworkwithclusters.dxbkrcp.mongodb.net/?retryWrites=true&w=majority&appName=myfirstworkwithclusters"


def main():
    client = MongoClient(uri, tlsCAFile=certifi.where())

    db = client['test']
    mops_coll = db['mops']
    crayfish_coll = db['crayfish']

    mops_coll.insert_one({'_id': str(uuid4()), 'name': 'Mops', 'price': 100})
    mops_coll.insert_one({'_id': str(uuid4()), 'name': 'Gig', 'price': 200})

    print('Hello, World!')

if __name__ == '__main__':
    main()