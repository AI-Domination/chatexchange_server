# ChatExchange Server

This repo contains a simple Python server for [ChatExchange](https://github.com/Manishearth/ChatExchange).

**By default, there is NO authenticion for requesets to the server**.

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

Create a Docker secret baesd on that file:

```bash
docker secret create chatexchange_config config.ini
```

Then run the container:

```bash
docker run -p 127.0.0.1:8000:8000 --secret source=chatexchange_config,target=/run/secerts/config.ini chatexchange_server
```
