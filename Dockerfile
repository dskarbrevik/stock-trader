FROM python:3.8-slim-buster

# WORKDIR /app
# COPY . .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
