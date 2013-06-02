import tornado.ioloop
import tornado.web
import riak
import uuid
import urlparse
import json

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

        riak_query = build_riak_query(query)
        if riak_query is None:
            self.send_error(status_code=403)
            return

        accident_search = rk.search('collisions', riak_query).run()

        res = [a.get().get_data() for a in accident_search]
        for acc in res:
            for k, v in acc.items():
                if k.endswith('_num'):
                    acc[k[:-4]] = acc[k]
                    del acc[k]

        self.write(json.dumps([a.get().get_data() for a in accident_search]))
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


application = tornado.web.Application([
    (r"/api/1/report", ReportHandler),
])

if __name__ == "__main__":
    application.listen(14441)
    tornado.ioloop.IOLoop.instance().start()
