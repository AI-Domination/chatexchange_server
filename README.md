# ChatExchange Server

> [!WARNING]
> There is no authentication for this. It is _highly_ advised that you exclusively use this on entirely trusted machines on entirely trusted networks. In addition, consider modifying it to only listen on localhost.

This repo contains a simple Python server for [ChatExchange](https://github.com/Manishearth/ChatExchange).

## Docker setup

Build the container:

```bash
docker build -t chatexchange_server .
```

Create a file with your desired config:

```ini
[config]
email = you@example.com
password = abcd1234
room_id = 12345
```

Create a Docker secret based on that file:

```bash
docker secret create chatexchange_config config.ini
```

Then run the container:

```bash
docker run -p 127.0.0.1:8000:8000 --secret source=chatexchange_config,target=/run/secerts/config.ini chatexchange_server
```
