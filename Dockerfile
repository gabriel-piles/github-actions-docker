FROM python:3.9-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser appuser
RUN mkdir /home/appuser/docker_volume
RUN chown appuser:appuser /home/appuser/docker_volume

RUN touch service.log

USER appuser
WORKDIR /home/appuser

COPY --chown=appuser . .

ENV FLASK_APP app.py

CMD gunicorn -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:5050

