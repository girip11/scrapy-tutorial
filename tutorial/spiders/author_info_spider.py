from dataclasses import dataclass
from typing import Optional

import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector import Selector
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError, TimeoutError


@dataclass
class Author:
    name: str
    born_date: Optional[str]
    born_location: Optional[str]


# yield an object to mark as the response of scraping a URL
# yield a Request object by callilng response.follow so that scrapy continues to scrap those pages


class AuthorSpider(scrapy.Spider):
    # provide name to the Spider.
    # Overrides the base class attribute
    name = "authors"

    # This should contain the URLS to crawl
    # Base class expects this attribute to be populated
    start_urls = ["http://quotes.toscrape.com"]

    authors: set[str] = set()

    def parse(self, response: HtmlResponse, **kwargs):
        self.logger.info("Hello from my quotes spider")

        # we can also use xpath selectors
        quotes = response.css("div.quote")
        for quote in quotes:
            # use `.get` only to obtain a string
            # .get() always returns a single result; if there are several matches, content of a
            # first match is returned; if there are no matches, None is returned. .getall() returns
            # a list with all results.
            author_name = quote.css(".author::text").get(default="").strip()

            if author_name and author_name not in self.authors:
                self.authors.add(author_name)
                author_link = quote.css("a::attr(href)").get()
                self.logger.info(f"Crawling details of the author {author_name}")
                request = response.follow(
                    author_link,
                    callback=self._parse_author_details,
                    errback=self.errback,
                    # https://docs.scrapy.org/en/latest/topics/request-response.html#request-meta-special-keys
                    meta={"author_link": author_link},
                )
                request.cb_kwargs["author_name"] = author_name
                yield request

        yield from self._parse_next(response)

    def _parse_author_details(self, response: HtmlResponse, **kwargs):
        author_details: Selector = response.css("div.author-details")

        in_author_name: Optional[str] = kwargs.get("author_name", None)

        if response.meta is not None:
            self.logger.info(
                f"Author page link {response.meta.get('author_link', None)}"
            )

        author_name: str = author_details.css(".author-title::text").get("").strip()
        self.logger.info(
            f"Expected author name: {in_author_name}, actual author name: {author_name}"
        )

        if author_name == in_author_name:
            self.logger.info(f"Returning the details of {author_name}")
            yield Author(
                author_name,
                author_details.css(".author-born-date::text").get(),
                author_details.css(".author-born-location::text").get(),
            )

    def _parse_next(self, response: HtmlResponse):
        # crawl subsequent pages
        # use the URL from the .next class. Examine the webpage using browser devtools
        for next_url in response.css("li.next a::attr(href)").getall():
            self.logger.info(f"Crawling author details from {next_url}")
            # response.follow supports relative URLS
            yield response.follow(next_url, callback=self.parse)

    def errback(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error("DNSLookupError on %s", request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error("TimeoutError on %s", request.url)
