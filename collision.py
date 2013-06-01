import tornado.ioloop
import tornado.web
import riak

class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        print 'getting accident report'

    def post(self):
        print 'received new accident report'

application = tornado.web.Application([
    (r"/1/report", ReportHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
