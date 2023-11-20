import requests
import json
import csv


geojson_url = 'https://data.smartdublin.ie/dataset/6cbabf95-6b81-48e7-a2b8-b2345bbe80a1/resource/68e46a6b-383c-4f67-888c-95210e695df1/download/dcc_public_bin_locations.geojson'


response = requests.get(geojson_url)

if response.status_code == 200:
    data = response.json()


    with open('BinLocations.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)


        csv_writer.writerow(['Bin_ID', 'Bin_Type', 'Electoral_Area', 'Irish_X', 'Irish_Y'])

        for feature in data['features']:
            properties = feature['properties']
            coordinates = feature['geometry']['coordinates']

            bin_id = properties['Bin_ID']
            bin_type = properties['Bin_Type']
            electoral_area = properties['Electoral_Area']
            irish_x = coordinates[0]
            irish_y = coordinates[1]


            csv_writer.writerow([bin_id, bin_type, electoral_area, irish_x, irish_y])
else:
    print("Failed to fetch the GeoJSON file.")
