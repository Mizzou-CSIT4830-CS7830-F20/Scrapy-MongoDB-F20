import scrapy 

#from brickset.items from BricksetItem
from .. import items

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://brickset.com/sets/year-2020']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    
    def parse(self, response):
        SET_SELECTOR = '.set'
        
        for brickset in response.css(SET_SELECTOR):
            
            NAME_SELECTOR = "div h1 ::text"
            PIECES_SELECTOR = ".//dl[dt/text() = 'Pieces']/dd/a/text()"
            MINIFIGS_SELECTOR = ".//dl[dt/text() = 'Minifigs']/dd[2]/a/text()"
            IMAGE_SELECTOR = "img ::attr(src)"
            
            item = items.BricksetItem()
            
            item['name'] = brickset.css(NAME_SELECTOR).extract_first()
            item['pieces'] = brickset.xpath(PIECES_SELECTOR).extract_first()
            item['minifigs'] = brickset.xpath(MINIFIGS_SELECTOR).extract_first()
            item['image'] = brickset.css(IMAGE_SELECTOR).extract_first()
            
            yield item
            
#            yield {
#                'name': brickset.css(NAME_SELECTOR).extract_first(),
#                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#            }
        

#        NEXT_PAGE_SELECTOR = ".next a ::attr(href)"
#        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#        if next_page: 
#            yield scrapy.Request(
#                response.urljoin(next_page),
#                callback=self.parse
#            )
#        else:
#            NEXT_YEAR_SELECTOR = ".browselinks .col a ::attr(href)"
#            all_years = response.css(NEXT_YEAR_SELECTOR).extract()
#            
#            print("all years = ", all_years)
#            
#            if len(all_years) > 2:
#                next_year = all_years[-1]
#                
#                if next_year: 
#                    print("next_year = ", next_year)
#                    
#                    yield scrapy.Request(
#                        response.urljoin(next_year),
#                        callback = self.parse
#                    )
#            else:
#                print("End of program")
