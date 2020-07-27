FROM python:3.8-alpine

RUN apk add --no-cache bash gcc git jq libffi-dev musl-dev openssl-dev util-linux yaml-dev
RUN pip install --upgrade pip
RUN pip install ansible

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
