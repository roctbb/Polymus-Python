import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Привет мир!")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("Привет, {0}!".format(name))

settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()