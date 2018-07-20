from pymongo import MongoClient
from multiprocessing import Pool

def get_ekwing():
    mongo_client = MongoClient('10.200.2.212')
    ekwing = mongo_client['ekwing']
    return ekwing


def get_data_from_city_id(city_id):
    ekwing = get_ekwing()
    city = ekwing.city.find_one({'_id': city_id})
    print city['_id']


def main():
    p = Pool(10)
    ekwing = get_ekwing()
    all_citys_ids = [city['_id'] for city in ekwing.city.find({}, {'_id': 1})]
    p.map(get_data_from_city_id, all_citys_ids)
    p.close()
    p.terminate()
    p.join()


if __name__ == '__main__':
    main()
