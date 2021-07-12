# Scrapy Shell

> The shell is used for testing XPath or CSS expressions and see how they work and what data they extract from the web pages you’re trying to scrape. It allows you to interactively test your expressions while you’re writing your spider, without having to run the spider to test every change.
> Once you get familiarized with the Scrapy shell, you’ll see that it’s an invaluable tool for developing and debugging your spiders.

- If you have **IPython** installed, the Scrapy shell will use it. IPython is recommended.

```scrapy.cfg
[settings]
shell = ipython
```

- Launch the scrapy shell using `scrapy shell <url_or_uri_to_local_html_file> --nolog`. We get a shell with the following variables populated.

![Scrapy shell variables](assets/scrapy_shell_objects.png)

- `scrapy shell file:///absolute/path/to/file.html` - File URI example.

## Useful Shortcuts

- `shelp` - available objects and shortcuts
- `view(response)` - opens the response in browser
- `fetch(url[, redirect=True])` or `fetch(request)` - fetch a new response from the given URL and update all related objects accordingly. You can optionaly ask for HTTP 3xx redirections to not be followed by passing `redirect=False`

## Invoking shell from scrapy spider

```Python
import scrapy


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        # Rest of parsing code.
```

- In this scrapy shell, you can only inspect and play around with the response or view it. We cannot make new requests using `fetch`
- Hit `Ctrl-D (or Ctrl-Z in Windows)` to exit the shell and resume the crawling.

---

## References

- [Scrapy shell](https://docs.scrapy.org/en/latest/topics/shell.html)
