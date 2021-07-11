# Spider

- Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).

## What's done in a spider?

- The first requests to perform are obtained by calling the `start_requests()` method which (by default) generates `Request` for the URLs specified in the `start_urls` attribute and the `parse` method as callback function for the Requests.

- In the `**callback function**, you parse the response (web page) and return item objects, Request` objects, or an iterable of these objects.

- In the callback functions, you parse the page contents, typically using `Selectors`

- Finally, the items returned from the spider will be typically persisted to a database (in some **Item Pipeline**) or written to a file using **Feed exports**.

## Examples

- [Quote spider](../tutorial/spiders/quotes_spider.py)
- [Author spider](../tutorial/spiders/author_info_spider.py)

## Pass arguments to Spider from commandline

- `scrapy crawl <spider_name> -a arg=value`. The arguments can be accessed via the spider's `__init__`

- The default `__init__` method will take any spider arguments and copy them to the spider as attributes. We can access using `self.arg` inside the spider object.

```Python
class CustomSpider(scrapy.Spider):
    name = "custom_spider"

    def __init__(self, arg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arg = arg
```

## Spider types

- `scrapy.spiders.Spider`

Scrapy comes with some useful generic spiders that you can use to subclass your spiders from.

- `scrapy.spiders.CrawlSpider` - [example](https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider-example)

- `scrapy.spiders.XMLFeedSpider` - to parse XML feeds

- `scrapy.spiders.CSVFeedSpider` - Iterates over csv rows

- `scrapy.spiders.SitemapSpider`

---

## References

- [Spider in scrapy](https://docs.scrapy.org/en/latest/topics/spiders.html)
