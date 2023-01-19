# ChatExchange Server

This repo contains a simple Python server for [ChatExchange](https://github.com/Manishearth/ChatExchange).

**By default, there is NO authenticion for requesets to the server**, so I'd only suggest having it listen on `localhost`, and even only do that if you are totally sure nobody can make malicous requests to `localhost`.

It listens on `localhost:8000`, and when it receives a `GET` request such as `http://localhost:8000/?Hello%20world`, it will post `Hello world` in the chatroom it is set to use.

The envoirnment variables `CHATEXCHANGE_EMAIL` and `CHATEXCHANGE_PASS` should be set to your email + password for Stack Exchange, and `CHATEXCHANGE_ROOM` should be the SE chatroom ID to post messages to.

Usage:
```none
$ pip install bottle chatexchange
...
$ CHATEXCHANGE_EMAIL=you@example.com CHATEXCHANGE_PASS=PasswordGoesHere CHATEXCHANGE_ROOM=141447 python3 main.py
```
