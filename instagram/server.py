import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = [
    ('/', MainHandler),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()