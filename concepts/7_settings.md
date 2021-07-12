# Scrapy Settings

- We can customize spiders, extensions, pipelines.

- `SCRAPY_SETTINGS_MODULE` environment variable. Settings is a python module and it should be in the python import search path.

## Different settings

- Command line options (most precedence)

- Settings per-spider

- Project settings module (`settings.py` within the project directory.)

- Default settings per-command

- Default global settings (less precedence) - [Builtin global setting](https://docs.scrapy.org/en/latest/topics/settings.html#built-in-settings-reference) located at `scrapy.settings.default_settings`.

## Accessing settings from Spider

```Python
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://example.com']

    def parse(self, response):
        print(f"Existing settings: {self.settings.attributes.keys()}")
```

- The settings attribute is set in the base `Spider` class after the spider is initialized. If you want to use the settings before the initialization (e.g., in your spider’s `__init__()` method), you will need to override the `from_crawler()` method.

## Accessing settings in Extensions, middlewares and Pipelines

- Settings can be accessed through the `scrapy.crawler.Crawler.settings` attribute of the Crawler that is passed to from_crawler method in extensions, middlewares and item pipelines:

---

## References

- [Scrapy Settings](https://docs.scrapy.org/en/latest/topics/settings.html)
