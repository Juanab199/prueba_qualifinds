FROM python:3.10

WORKDIR /src

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --upgrade pip==24.3.1 && pip install -r requirements.txt

COPY src /src

RUN pytest

USER root
RUN chmod u+x /src/gunicorn.sh

RUN useradd -ms /bin/sh admin
USER admin

EXPOSE 8080

ENTRYPOINT [ "sh", "/src/gunicorn.sh" ]