from typing import Optional, Awaitable
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.render("index.html")


main_pattern = (r"/", MainHandler)
