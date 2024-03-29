FROM python:3.9-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser appuser

USER appuser
WORKDIR /home/appuser

COPY --chown=appuser . .

#USER root
#RUN rm -rf /home/appuser/docker_volume

#RUN mkdir /home/appuser/docker_volume
#RUN chmod -777 /home/appuser/docker_volume

#RUN touch /home/appuser/docker_volume/service.log

ENV FLASK_APP app.py
CMD gunicorn -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:5050

