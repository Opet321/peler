FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt update && apt upgrade -y; apt-get install git curl zip neofetch ffmpeg -y

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r req* 

EXPOSE 8080

CMD ["bash", "start.sh"]
