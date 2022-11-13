from typing import Optional, Awaitable, Union

from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler


class RoomSocketHandler(WebSocketHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def on_message(self, message: Union[str, bytes]) -> Optional[Awaitable[None]]:
        pass

    def __init__(self, room_pin):
        self.room_pin = room_pin


class RoomsHandler(RequestHandler):
    rooms = dict()

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.render("rooms.html", rooms=RoomsHandler.rooms.keys())

    def post(self, *args, **kwargs):
        if kwargs.get('room_pin'):
            room = RoomSocketHandler(kwargs['room_pin'])
            RoomsHandler.rooms[room.room_pin] = room

        self.render("rooms.html", rooms=RoomsHandler.rooms.keys())
