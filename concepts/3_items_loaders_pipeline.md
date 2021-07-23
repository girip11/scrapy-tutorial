# Items, Item loaders and Item pipelines

## Items

Scrapy supports following item types

- dictionary `{}`
- `dataclass` objects
- `scrapy.item.Item`. You can extend Items (to add more fields or to change some metadata for some fields) by declaring a subclass of your original Item.

```Python
from scrapy.item import Item, Field

class CustomItem(Item):
    one_field = Field()
    another_field = Field()
```

- `attr.s` from `attrs` package

```Python
import attr

@attr.s
class CustomItem:
    one_field = attr.ib()
    another_field = attr.ib()
```

## Unifying all item types with common interface

Since item object can be a dict or instance of `Item`, dataclass etc, its always recommended to use the `scrapy.itemadapter.ItemAdapter(item: Any)` to work with items.

## Item loaders

Think of item loader as a **builder**(builder design pattern) for building the item.

```Python
from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    # Product can be subclassof Item or a dataclass
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()
```

`Item` class can have input and output coprocessors defined.

```Python
import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value

class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )
```

Nested loaders can be created using `loader_instance.nested_xpath` or `loader_instance.nested_css`

## Item pipeline

---

## References

- [Items](https://docs.scrapy.org/en/latest/topics/items.html)
- [Item loaders](https://docs.scrapy.org/en/latest/topics/loaders.html)
