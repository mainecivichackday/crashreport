import requests
import json
import datetime

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
        'location_start': l[6].replace('"', '').strip(),
        'location_end': l[8].replace('"', '').strip(),
        'county': '',
        'town': l[0],
        'notes': '',
        'state_rank': l[-2],
        'county_rank': l[-1],
        'total_crashes': l[-4],
        'crf': l[-3],
        'time': datetime.datetime(year=2009, month=1, day=1).strftime(
            '%Y-%m-%dT%H:%M:%S')
    }

    #requests.post('http://localhost:14441/api/1/report', data=json.dumps(accident))
    requests.post('http://evilteam.com/api/1/report', data=json.dumps(accident))
