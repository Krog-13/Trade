FROM python:3.10
RUN adduser yskill
WORKDIR /home/yskill

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
RUN chmod +x boot.sh

ENV FLASK_APP portfolio.py

RUN chown -R yskill:yskill ./
USER yskill

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
CMD ["venv/bin/python", "main.py"]