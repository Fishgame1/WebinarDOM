FROM python:3.5
ENV PYTHON_VERSION 3.5.7
# created based on https://github.com/joyzoursky big thanks for his job!
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip


# copy files
RUN mkdir /WebinarDOM
WORKDIR /WebinarDOM
ADD . /WebinarDOM

# unpack chromedriver
RUN unzip -o /tmp/chromedriver.zip chromedriver -d /WebinarDOM

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
