from chatexchange import client, Client, rooms
from bottle import route, request, run
from os import environ
from urllib.parse import unquote

chat_client: client.Client = Client(
    "stackexchange.com", environ["CHATEXCHANGE_EMAIL"], environ["CHATEXCHANGE_PASS"]
)

room: rooms.Room = chat_client.get_room(
    int(
        environ["CHATEXCHANGE_ROOM"]
    )
)


@route("/")
def index():
    text = unquote(request.query_string)
    room.send_message(text)


run(host="localhost", port=8000, debug=True)
