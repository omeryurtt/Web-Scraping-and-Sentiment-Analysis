import scrapy
from ..items import CommentsItem
from urllib.parse import urljoin
from ..asin_list import get_asin_list

class AmazonSpiderSpider(scrapy.Spider):

    name = "amazon"

    def start_requests(self):
        asin_list = get_asin_list()

        for asin in asin_list:
            amazon_reviews_url = f"https://www.amazon.com/product-reviews/{asin}/"
            yield scrapy.Request(
                url=amazon_reviews_url,
                callback=self.parse_reviews,
                meta={'asin': asin, 'retry_count': 0}
            )

    def parse_reviews(self, response):
        asin = response.meta["asin"]
        retry_count = response.meta["retry_count"]

        next_page_relative_url = response.css(".a-pagination .a-last>a::attr(href)").get()
        if next_page_relative_url is not None:
            retry_count = 0
            next_page = urljoin("https://www.amazon.com/", next_page_relative_url)
            yield scrapy.Request(url=next_page, callback=self.parse_reviews,
                                 meta={"asin": asin, "retry_count": retry_count}
                                 )


        elif retry_count < 3:
            retry_count = retry_count + 1
            yield scrapy.Request(url=response.url, callback=self.parse_reviews, dont_filter=True,
                                 meta={'asin': asin, 'retry_count': retry_count}
                                 )


        review_elements = response.css("#cm_cr-review_list div.review")
        for review_element in review_elements:
            item = CommentsItem()
            item["asin"] = asin
            item["user_name"] = review_element.css(".a-profile-name::text").get()
            item["review_star"] = review_element.css("*[data-hook*=review-star-rating] ::text").re(r"(\d+\.*\d*) out")[0]
            item["review_title"] = review_element.css("*[data-hook=review-title]>span::text").get()
            item["text"] = "".join(review_element.css("span[data-hook=review-body] ::text").getall()).strip()
            item["date_and_country"] = review_element.css("span[data-hook=review-date] ::text").get()
            item["product_name"] = review_element.css(".a-size-mini::text").get()

            yield item
