FROM python:3.8
WORKDIR /home/app
COPY requirements.txt requirements.txt
COPY config.py config.py
COPY credential.json credential.json
COPY main.py main.py
COPY .env .env
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
COPY src src
COPY web web
EXPOSE 5000
ENTRYPOINT [ "venv/bin/python" ]
CMD [ "main.py" ]
