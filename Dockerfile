FROM python:3.11.4-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "clck.py" ]