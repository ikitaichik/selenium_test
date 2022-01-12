FROM python:3.7.2-alpine3.8

RUN pip install selenium

RUN apk add chromium
RUN apk add chromium-chromedriver

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/

# create an entrypoint.sh whith this command: python "${@}"
COPY selenium_GCP.py /
ENTRYPOINT ["python3.7", "selenium_GCP.py"]
