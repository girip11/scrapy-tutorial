# CSS selectors

## Extensions to CSS Selectors

Per W3C standards, CSS selectors do not support selecting text nodes or attribute values. But selecting these is so essential in a web scraping context that Scrapy (parsel) implements a couple of non-standard pseudo-elements:

- to select text nodes, use `::text`

- to select attribute values, use `::attr(name)` where name is the name of the attribute that you want the value of

---

## References

- [CSS selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
