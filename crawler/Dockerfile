FROM python:3.10

WORKDIR /usr/src/crawler

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["scrapy", "crawl", "sreality_spider"]
