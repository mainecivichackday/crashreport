# This requires:
# - Tornado
# - PyWAPI

import tornado.ioloop
import tornado.web
import tornado.template
import pywapi
import string
import json
from datetime import datetime

import riak
import uuid
import urlparse

TLoader = tornado.template.Loader("./");

rk = riak.RiakClient()

rkb = rk.bucket('collisions')

NUMERIC_FIELDS = ['county_rank', 'crf', 'latitude', 'longitude',
    'state_rank', 'total_crashes']

SEARCHABLE_FIELDS = ['town', 'county', 'notes', 'crf', 'total_crashes',
    'state_rank', 'county_rank', 'location_start', 'location_end']

def build_riak_query(query):
    for field in NUMERIC_FIELDS:
        if '{}_start'.format(field) in query and '{}_end'.format(field) in query:
            start = query['{}_start'.format(field)][0]
            end = query['{}_end'.format(field)][0]
            return '{}:[{} TO {}]'.format(field, start, end)

    for field in SEARCHABLE_FIELDS:
        if field in query:
            return '{}:{}'.format(field, query[field][0])

    return None


class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        query = urlparse.parse_qs(self.request.query)

        res = [rkb.get(k).get_data() for k in rkb.get_keys()]

        riak_query = build_riak_query(query)
        if riak_query is not None:
            accident_search = rk.search('collisions', riak_query).run()
            res = [a.get().get_data() for a in accident_search]

        for acc in res:
            for k, v in acc.items():
                if k.endswith('_num'):
                    acc[k[:-4]] = acc[k]
                    del acc[k]

        self.write(json.dumps(res))
        self.finish()

    def post(self):
        accident_id = uuid.uuid4().hex
        accident = json.loads(self.request.body)
        
        # force riak to treat certain fields as numeric
        for k, v in accident.items():
            if k in NUMERIC_FIELDS:
                accident[k + '_num'] = accident[k]
                del accident[k]

        acc = rkb.new(accident_id, data=accident)
        acc.store()


class MainHandler(tornado.web.RequestHandler):
        def get(self):
                self.write(TLoader.load("index.htm").generate())
                self.finish()
        def post(self):
                town = self.get_argument("town");
                county = self.get_argument("county");
                state = self.get_argument("state");
                location = self.get_argument("location");
                latitude = self.get_argument("latitude");
                longitude = self.get_argument("longitude");
                time = datetime.now();
                fatalities = self.get_argument("fatalities");
                weather_dic = pywapi.get_weather_from_yahoo(pywapi.get_location_ids(town + ", " + state).keys()[0]);
                weather = (weather_dic['condition']['text']) + ", " + (weather_dic['condition']['temp']) + "C.";
                crashinfo = json.dumps({'town': town, 'county': county, 'state': state, 'location': location, 'latitude': latitude, 'longitude': longitude, 'time': tim$
                self.write(crashinfo)
                self.finish()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/api/1/report", ReportHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': './'})
])

if __name__ == "__main__":
        application.listen(8888);
        tornado.ioloop.IOLoop.instance().start();
