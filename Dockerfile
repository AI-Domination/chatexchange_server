FROM python:3.11
RUN pip install --no-cache-dir --upgrade chatexchange bottle python-dotenv
WORKDIR /
RUN git clone https://github.com/AI-Domination/chatexchange_server.git
WORKDIR /chatexchange_server
EXPOSE 80
ENTRYPOINT [ "python3", "main.py" ]
