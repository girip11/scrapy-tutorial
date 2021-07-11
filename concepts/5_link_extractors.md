# Link extractors

Link extractor can be used to extract all the links from a given response.

- `scrapy.linkextractors.LinkExtractor`

## Usage

```Python
link_extractor = LinkExtractor(allow=('item\.php', ), deny=('subsection\.php', ))

links = link_extractor.extract_links(response)
```

Each link object is an instance of [`Link`](https://docs.scrapy.org/en/latest/topics/link-extractors.html#scrapy.link.Link)

## Rule

- Using `scrapy.spiders.Rule` along with `LinkExtractor` we can extract links from responses and make requests to those links and parse those responses.

```Python
 rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )
```

- `Rule` is used in `CrawlSpider`

---

## References

- [Link extractors](https://docs.scrapy.org/en/latest/topics/link-extractors.html)
