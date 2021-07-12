# Feed exports

- Supported formats are json, json lines, csv and xml.

- Supported storages are GCS, AWS S3, console, ftp, local filesystem.

## Delayed file delivery

These storage backends do not upload items to the feed URI as those items are scraped. Instead, Scrapy writes items into a temporary local file, and only once all the file contents have been written (i.e. at the end of the crawl) is that file uploaded to the feed URI.

If you want item delivery to start earlier when using one of these storage backends, use `FEED_EXPORT_BATCH_ITEM_COUNT` to split the output items in multiple files, with the specified maximum item count per file. That way, as soon as a file reaches the maximum item count, that file is delivered to the feed URI, allowing item delivery to start way before the end of the crawl.

[Feed export settings](https://docs.scrapy.org/en/latest/topics/feed-exports.html#std-setting-FEED_EXPORTERS)

---

## References

- [Feed exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html)
