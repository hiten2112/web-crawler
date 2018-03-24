import scrapy

class spider1(scrapy.Spider):
    name = 'site_name'
    start_urls = ['website_link_from_information_is_being_fetched']

    def parse(self, response):
        #Extract product information
       titles = response.css('img::attr(title)').extract()
       images = response.css('img::attr(data-img)').extract()
       prices = response.css('.p_price::text').extract()
       discounts = response.css('.prd_discount::text').extract()


       for item in zip(titles,prices,images,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : [item[2])], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info
