# Dockerfile
# FROM python:3.8

# RUN apt-get update && apt-get clean

# # install system dependencies
# RUN apt-get update \
#     && apt-get -y install gcc make \
#     && rm -rf /var/lib/apt/lists/*s

# # install google chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get -y update
# RUN apt-get install -y google-chrome-stable

# # install chromedriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# # # set display port to avoid crash
# ENV DISPLAY=:99

# WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt
# RUN pip3 install -r /app/requirements.txt

# COPY . .


# CMD ["python","./src/query_handling.py"]

# run command
# docker run -v /dev/shm:/dev/shm --shm-size=2gb dsa-search:1.0

#<----------------------NODE -------------------------->

#node application part
FROM node:16

WORKDIR /app

COPY ./package.json ./
RUN python3 --version

RUN npm install -g npm@8.10.0
RUN npm install 

COPY . .

EXPOSE 3000

CMD ["node","./app.js"]

# docker run -it --init -v $(pwd):/app -p 3000:3000 dsa-server:1.0
