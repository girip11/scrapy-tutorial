# Requests and responses

> Typically, `Request` objects are generated in the spiders and pass across the system until they reach the Downloader, which executes the request and returns a `Response` object which travels back to the spider that issued the request.

## [Request](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request)

- `scrapy.http.Request` aka `scrapy.Request`

- `scrapy.http.Request(url, callback, errback, http_method, meta, body, headers, cookies ...)`

- `scrapy.http.Request.replace(...)` - modify current object with few parameters changes. For instance, different URL with same headers, cookies etc.

- We can create `Request` object from `curl` command too.

### Request subclasses

- `scrapy.http.FormRequest` - we can pass a form data to the request.

> It is usual for web sites to provide pre-populated form fields through `<input type="hidden">` elements, such as session related data or authentication tokens (for login pages). When scraping, you would want these fields to be automatically pre-populated and only override a couple of them, such as the user name and password. You can use the `FormRequest.from_response()` method for this job.

- `scrapy.http.JsonRequest` - serializes the data in to JSON body.

## Response

- [`scrapy.http.Response`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response)

Important methods

- `urljoin`
- `follow`
- `follow_all`

### Response subclasses

- `scrapy.http.TextResponse`
- `scrapy.http.HtmlResponse`
- `scrapy.http.XmlResponse`

---

## References

- [Request and responses](https://docs.scrapy.org/en/latest/topics/request-response.html)
