FROM alpine:3.9

ARG GIT_COMMIT_SHA='Undefined'

ENV DEBUG false
ENV ENV_GIT_COMMIT_SHA=${GIT_COMMIT_SHA}

RUN apk add --update python3

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "./server.py" ]