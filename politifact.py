import scrapy


class PolitifactMenShoesSpider(scrapy.Spider):
    name = "politifacty"
    start_urls = ['https://www.politifact.com/truth-o-meter/statements/']
    allowed_domains = ['www.politifact.com']

    def parse(self, response):
        for product in response.css("div.scoretable__item"):

            yield {
                "Titles": product.css("div.mugshot img::attr('alt')").extract_first(),
               "Description": product.css("a.link::text").extract_first(),
               "Image": product.css("div.meter img::attr('alt')").extract_first(),
               "Date": product.css("span.article__meta::text").extract_first(),
               "URL": "https://www.politifact.com" + '' + product.css("p.statement__text a::attr('href')").extract_first()
            }
        next_url_path = response.css(
             "a.step-links__next::attr('href')").extract_first()
        if next_url_path:
            yield scrapy.Request(
            response.urljoin(next_url_path),
            callback=self.parse
            )


# scrapy crawl politifacty -o politifacty5-11.csv

