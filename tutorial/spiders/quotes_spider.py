from dataclasses import dataclass
from typing import Optional

import scrapy
from scrapy.http.response.html import HtmlResponse


@dataclass
class Quote:
    text: str
    author: str
    tags: Optional[list[str]]


class QuotesSpider(scrapy.Spider):
    # provide name to the Spider.
    # Overrides the base class attribute
    name = "quotes"

    # This should contain the URLS to crawl
    # Base class expects this attribute to be populated
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response: HtmlResponse, **kwargs):
        self.logger.info("Hello from my quotes spider")

        quotes = response.css("div.quote")

        for quote in quotes:
            # use `.get` only to obtain a string
            yield Quote(
                quote.css(".text::text").get(),
                quote.css(".author::text").get(),
                quote.css(".tag::text").getall(),
            )

        yield from self._parse_next(response)

    def _parse_next(self, response: HtmlResponse):
        # crawl subsequent pages
        # use the URL from the .next class. Examine the webpage using browser devtools
        for next_url in response.css("li.next a::attr(href)").getall():
            self.logger.info(f"Crawling URL: {next_url}")
            # response.follow supports relative URLS
            yield response.follow(next_url, callback=self.parse)
