# This requires:
# - Tornado
# - PyWAPI

import tornado.ioloop
import tornado.web
import tornado.template
import pywapi
import string
from datetime import datetime

TLoader = tornado.template.Loader("./");

class MainHandler(tornado.web.RequestHandler):
        def get(self):
                self.write(TLoader.load("index-form.htm").generate());
        def post(self):
                town = self.get_argument("town");
                county = self.get_argument("county");
                state = self.get_argument("state");
                location = self.get_argument("location");
                latitude = self.get_argument("latitude");
                longitude = self.get_argument("longitude");
                time = datetime.now();
                fatalities = self.get_argument("fatalities");
                weather_dic = pywapi.get_weather_from_yahoo("USME0017");
                weather = (weather_dic['condition']['text']) + ", " + (weather_dic['condition']['temp']) + "C.";
                self.write(TLoader.load("post.htm");
application = tornado.web.Application([(r"/", MainHandler),])

if __name__ == "__main__":
        application.listen(8888);
        tornado.ioloop.IOLoop.instance().start();
