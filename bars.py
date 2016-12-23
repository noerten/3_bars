import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data

def get_biggest_bar(data):
    biggest_bar_obj = max(data, key=lambda i: i['SeatsCount'])
    return biggest_bar_obj['Name']    

def get_smallest_bar(data):
    smallest_bar_obj = min(data, key=lambda i: i['SeatsCount'])
    return smallest_bar_obj["Name"]  

def get_closest_bar(data, longitude, latitude):
    for bar in data:
        #bar_coords - list with longitude and latitude
        bar_coords = bar['geoData']['coordinates']
        bar['dist_to_user'] = ((bar_coords[0] - longitude) ** 2
            + (bar_coords[1] - latitude) ** 2) ** (1/2)
    closest_bar_obj = min(data, key=lambda i: i['dist_to_user'])
    return closest_bar_obj['Name']
                          
if __name__ == '__main__':
    file_name = input('Enter file name/path: ')
    data = load_data(file_name)
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    print("smallest bar: {}\n"
          "biggest bar: {}\n".format(smallest_bar, biggest_bar))
    longitude = float(input('input longitude: '))
    latitude = float(input('input latitude: '))
    closest_bar = get_closest_bar(data, longitude, latitude)
    print('closest bar:', closest_bar)
