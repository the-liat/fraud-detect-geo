import time

import geopy
from IP2Location import IP2Location

ip_database_path = 'IP2LOCATION-LITE-DB9.BIN'

geolocator = geopy.Nominatim(user_agent='zipcode-finder')
ip_database = IP2Location(ip_database_path)


def convert_geo_location(lat, long):
    r = {}
    for i in range(3):
        try:
            r = geolocator.reverse(f'{lat}, {long}').raw['address']
        except Exception as e:
            time.sleep(2 - i)

    return dict(country=r.get('country', 'N/A'),
                zipcode=r.get('postcode', 'N/A'),
                county=r.get('county', 'N/A'),
                place=r.get('amenity', 'N/A'))


def convert_ip_address(ip_address):
    info = ip_database.get_all(ip_address)
    return dict(city=info.city,
                country=info.country_long,
                zipcode=info.zipcode,
                lat=info.latitude,
                long=info.longitude)


def main():
    data = open('data.csv').read()
    lines = data.split("\n")[:-1]
    records = []
    for line in lines[1:]:
        record = line.split(",")
        records.append(record)

    header = lines[0][:-1] + \
             "Country_GEO,County_GEO,zipcode_GEO,Place_GEO," \
             "Country_IP,City_IP,zipcode_IP,Lat_IP,Long_IP"

    filename = 'converted_GEO_location.csv'
    output = open(filename).read().split('\n')
    start = len(output) - 1
    for i, record in enumerate(records[start:]):
        index = start + i
        if index % 100 == 0:
            print(f'{index} / {len(records)}')
            '\n'.join(output)
            open(f'converted_GEO_location_{index}.csv', 'w').write('\n'.join(output))
        ip_address = record[1]
        lat = record[2]
        long = record[3]
        if lat != " ":
            x = convert_geo_location(lat, long)
            record += [x['country'], x['county'], x['zipcode'], x['place']]
        else:
            record += ["N/A"] * 4
        y = convert_ip_address(ip_address)
        record += [y['country'], y['city'], y['zipcode'], y['lat'], y['long']]
        output.append(','.join(record))
    final_output = '\n'.join(output)
    open('converted_GEO_location.csv', 'w').write(final_output)


if __name__ == '__main__':
    main()
