import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Привет мир!")

settings = [
    ('/', MainHandler),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()