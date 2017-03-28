import tornado.ioloop
import tornado.web
import random

class PhotosHandler(tornado.web.RequestHandler):
    def get(self):
        x = self.get_argument("x",0)
        y = self.get_argument("y", 0)

        #YOUR CODE

        self.write("{0} {1}".format(x,y))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = [
    ('/', MainHandler),
    ('/photos', PhotosHandler),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()