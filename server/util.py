import pickle
import json
import numpy as np

__data_columns = None
__locations = None
__model = None


def get_estimated_price(location, total_sqft, bath, balcony, bedrooms):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 1)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print('Loading Information')

    global __data_columns
    global __locations

    with open("./data/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations =  [x.lower() for x in __data_columns[4:]]

    global __model
    with open("./model/model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print('loading the model')
    


if __name__ == '__main__':
    load_saved_artifacts()
    get_location_names()
    print(get_estimated_price("1st Block Jayanagar", 1000, 3, 1, 4))
    print(get_estimated_price("Yelahanka New Town", 10000000, 6, 2, 9))