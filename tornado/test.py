import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Привет мир!")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("<h2 style='align: center; color: blue;'>Привет, {0}!</h1>".format(name))

class CatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("cat.html")

settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
    ('/cat', CatHandler),

    ('/cats/(.*)', tornado.web.StaticFileHandler, {'path': 'cats'}),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()