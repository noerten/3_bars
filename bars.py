import json
import os


def load_bars(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        bars = json.load(data_file)
    return bars


def get_biggest_bar(bars):
    biggest_bar_obj = max(bars, key=lambda i: i['SeatsCount'])
    return biggest_bar_obj['Name']


def get_smallest_bar(bars):
    smallest_bar_obj = min(bars, key=lambda i: i['SeatsCount'])
    return smallest_bar_obj["Name"]


def get_closest_bar(bars, longitude, latitude):
    for bar in bars:
        bar_longitude = bar['geoData']['coordinates'][0]
        bar_latitude = bar['geoData']['coordinates'][1]
        bar['dist_to_user'] = ((bar_longitude - longitude) ** 2 +
                               (bar_latitude - latitude) ** 2) ** (1/2)
    closest_bar_obj = min(bars, key=lambda i: i['dist_to_user'])
    return closest_bar_obj['Name']


if __name__ == '__main__':
    file_name = input('Enter file name/path: ')
    bars = load_bars(file_name)
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    print("smallest bar: {}\n"
          "biggest bar: {}\n".format(smallest_bar, biggest_bar))
    longitude = float(input('input longitude: '))
    latitude = float(input('input latitude: '))
    closest_bar = get_closest_bar(bars, longitude, latitude)
    print('closest bar:', closest_bar)
