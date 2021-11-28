FROM python:3


WORKDIR /usr/src/app


COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]