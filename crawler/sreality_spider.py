import scrapy
import psycopg2


class SRealitySpider(scrapy.Spider):
    name = 'SRealitySpider'
    # comprehension list of 25 (500 items) URLs  that the spider will start crawling from.    ( crawler sign)
    start_urls = ['https://www.sreality.cz/en/search/for-sale/apartments?page=' + str(i) + '&_escaped_fragment_='
                  for i in range(25)]

    def parse(self, response):
        # gets titles
        titles = response.xpath('.//*[@class="title"]/span/text()').getall()
        # gets url parts
        url_parts = response.xpath('.//*[@class="title"]/@href')
        for title, url_part in zip(titles, url_parts):
            # gets desired images
            img = response.xpath('.//a[@href="' + url_part.root + '"]/img/@src').getall()
            yield {
                    'url_part': url_part.root, "title": title, "img": img
                }