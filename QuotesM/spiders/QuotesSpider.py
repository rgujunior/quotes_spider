import scrapy
from scrapy.http import FormRequest
from QuotesM.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        login_url = 'http://quotes.toscrape.com/login'

        # Realiza o login
        FormRequest(login_url, formdata={'username': 'teste@teste.com', 'password': '12345'})

        for quote in response.css("div.quote"):
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            text = quote.css("span.text::text").get()

            if author == "Mark Twain" and "life" in tags:
                yield QuoteItem(author=author, tags=tags, text=text)

        # Regra 2: Quotes com a palavra "truth" no texto
        for quote in response.css("div.quote"):
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            text = quote.css("span.text::text").get()

            if "truth" in text:
                yield QuoteItem(author=author, tags=tags, text=text)

        # Paginação
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)