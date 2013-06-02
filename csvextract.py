import requests
import json

incsv = open('../crashdata.csv', 'r')

for line in incsv:
    ln = line.replace('\n', '')
    l = ln.split(',')
    if len(l) < 8:
        continue

    if l[1] == '' or l[2] == '':
        continue

    accident = {
        'latitude': l[1],
        'longitude': l[2],
        'location_start': l[6],
        'location_end': l[8],
        'county': '',
        'town': l[0],
        'notes': '',
        'state_rank': l[-2],
        'county_rank': l[-1],
        'total_crashes': l[-4],
        'crf': l[-3],
    }

    requests.post('http://localhost:14441/api/1/report', data=json.dumps(accident))
    #requests.post('http://evilteam.com/api/1/report', data=json.dumps(accident))

    #print accident['latitude'], accident['longitude'], accident['crf'], accident['county_rank'], accident['state_rank'], accident['town']
