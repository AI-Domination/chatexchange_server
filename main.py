from chatexchange import client, Client, rooms
from bottle import route, request, run
from urllib.parse import unquote
from configparser import ConfigParser

config = ConfigParser()
config.read("/run/secrets/chatexchange_config")

chat_client: client.Client = Client(
    "stackexchange.com", config.get("config", "email"), config.get("config", "password")
)

room: rooms.Room = chat_client.get_room(int(config.get("config", "room_id")))


@route("/")
def index():
    text = unquote(request.query_string)
    room.send_message(text)


run(host="0.0.0.0", port=80)
