import json

def load_data(filepath):
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data

def get_biggest_bar(data):
    biggest_seats = 0
    for i in data:
        seats = i['SeatsCount']
        if seats > biggest_seats:
            biggest_seats = seats
            biggest_bar = i['Name']
#    print(biggest_seats)
    return biggest_bar    

def get_smallest_bar(data):
    smallest_seats = float("inf")
    for i in data:
        seats = i['SeatsCount']
        if seats < smallest_seats:
            smallest_seats = seats
            smallest_bar = i['Name']
#    print(smallest_seats)
    return smallest_bar    

def get_closest_bar(data, longitude, latitude):
    smallest_dist = float("inf")
    for i in data:
        bar_longitude = i['geoData']['coordinates'][0]
        bar_latitude = i['geoData']['coordinates'][1]
        dist = ((bar_longitude - longitude) ** 2
                + (bar_latitude - latitude) ** 2) ** (1/2)
        if dist < smallest_dist:
            smallest_dist = dist
            closest_bar = i['Name']
#    print(dist)
    return closest_bar

if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    biggest_bar = get_biggest_bar(data)
    print('biggest bar', biggest_bar)
    smallest_bar = get_smallest_bar(data)
    print('smallest bar', smallest_bar)
    longitude = float(input('input longitude: '))
    latitude = float(input('input latitude: '))
    closest_bar = get_closest_bar(data, longitude, latitude)
    print('closest bar', closest_bar)
