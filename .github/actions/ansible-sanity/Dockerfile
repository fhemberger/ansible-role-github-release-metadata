FROM python:3.8-alpine

RUN apk add --no-cache bash gcc git libffi-dev musl-dev openssl-dev yaml-dev
RUN pip install --upgrade pip
RUN pip install ansible pycodestyle pylint voluptuous yamllint

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
