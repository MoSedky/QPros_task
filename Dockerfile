FROM python:latest
MAINTAINER sedky.cs@gmail.com
RUN apt-get update -y
RUN apt-get install -y wget xvfb unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable
ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
ENV PATH $CHROMEDRIVER_DIR:$PATH
COPY . /QPros_task
WORKDIR /QPros_task
ENV PYTHONPATH "/QPros_task"
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
CMD tail -f /dev/null