import time
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items  =["Item1", "Item2", "Item3"]
        self.render("template.html", title = "CASTOR SERVER", items = items)


def make_app():
    return tornado.web.Application([(r"/", MainHandler),])


app = make_app()
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
