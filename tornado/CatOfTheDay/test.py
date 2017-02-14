import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Привет мир!")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("<h2 style='align: center; color: blue;'>Привет, {0}!</h1>".format(name))

class CatHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            {"id": 1, "name": "Лунтик"},
            {"id": 2, "name": "Фирамир"},
            {"id": 3, "name": "Товарищ Буденый"},
            {"id": 4, "name": "Эльдар Джарахов"},
            {"id": 5, "name": "Кончик"},
            {"id": 6, "name": "Черный Вжух"},
        ]
        cat = random.choice(cats)
        self.render("cat.html", name=cat["name"], id=cat["id"])

settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
    ('/cat', CatHandler),

    ('/cats/(.*)', tornado.web.StaticFileHandler, {'path': 'cats'}),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()