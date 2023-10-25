from chatexchange import client, Client, rooms
from bottle import route, request, run
from urllib.parse import unquote
from configparser import ConfigParser
from dotenv import load_dotenv
from os import getenv


load_dotenv()

chat_client: client.Client = Client(
    "stackexchange.com", getenv("email"), getenv("password")
)

room: rooms.Room = chat_client.get_room(int(getenv("room_id")))


@route("/")
def index():
    text = unquote(request.query_string)
    room.send_message(text)


run(host="0.0.0.0", port=80)
