import tornado.ioloop
import tornado.web
import riak
import uuid
import urlparse
import json

rk = riak.RiakClient()

rkb = rk.bucket('collisions')

class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        query = urlparse.parse_qs(self.request.query)
        for k, v in query.items():
            if k not in ['town', 'county', 'notes']:
                self.send_error(status_code=403)
                self.finish()
                return

        town = query['town'][0]
        accident_search = rk.search('collisions', 'town:{}'.format(town)).run()

        self.write(json.dumps([a.get().get_data() for a in accident_search]))
        self.finish()

    def post(self):
        accident_id = uuid.uuid4().hex
        accident = json.loads(self.request.body)
        acc = rkb.new(accident_id, data=accident)
        acc.store()


application = tornado.web.Application([
    (r"/1/report", ReportHandler),
])

if __name__ == "__main__":
    application.listen(14441)
    tornado.ioloop.IOLoop.instance().start()
