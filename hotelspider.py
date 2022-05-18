import scrapy
import json


class HotelspiderSpider(scrapy.Spider):
    name = 'hotelspider'
    # allowed_domains = ['hotel']
    # start_urls = [
    #     "https://www.agoda.com/vi-vn/scent-premium-hotel/hotel/hanoi-vn.html?finalPriceView=1&isShowMobileAppPrice=false&cid=-1&numberOfBedrooms=&familyMode=false&adults=1&children=0&rooms=1&maxRooms=0&checkIn=2022-05-22&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=-1&showReviewSubmissionEntry=false&currencyCode=VND&isFreeOccSearch=false&flexibleDateSearchCriteria=[object%20Object]&isCityHaveAsq=false&tspTypes=1,1,16,16&los=1&searchrequestid=ecd00d3a-1279-44f9-b327-df0d03fa2f83"
    #     # 'https://www.agoda.com/vi-vn/sofitel-legend-metropole-hanoi-hotel/hotel/hanoi-vn.html',
    #     # 'https://www.agoda.com/vi-vn/hanoi-daewoo-hotel/hotel/hanoi-vn.html',
    #     # 'https://www.agoda.com/vi-vn/lotte-hotel-hanoi/hotel/hanoi-vn.html',
    #     # 'https://www.agoda.com/vi-vn/dolce-by-wyndham-hanoi-golden-lake/hotel/hanoi-vn.html']
    #
    f = open('e.json')
    start_urls = json.load(f)

    def parse(self, response):
        yield {
            'city': 'Hà Nội',
            'url': response.url,
            'name': response.css('h1.HeaderCerebrum__Name::text').get(),
            'address': response.css('span.HeaderCerebrum__Address ::text').get(),
            'stars': '5',
            # 'price': ,
            'ratings': response.css('div.ReviewScoreCompact__score > div > div > div > h3::text').get(),
            'number of reviewers': response.css('div.ReviewScoreCompact__detail > div.review-basedon > span.text ::text').get(),
            # 'facilities': response.css('div.Box-sc-kv6pi1-0.eqoTHM > p::text').getall(),
            'facilities': response.css('li.FavFeatures__Item.FavFeatures__Item--5 p::text').getall(),
            'description': response.css('div.Box-sc-kv6pi1-0.bhFfcp > p ::text').get(),
            # 'nearby_places':
        }

    # pass
    # def parse(self, response):
    #     yield
    #     {
    #         'city': 'Hà Nội',
    #         'url': response.url,
    #         'name': response.xpath('//*[@id="hp_hotel_name"]/text()')[1].get(),
    #         'address': response.css('#showMap2 > span.hp_address_subtitle.js-hp_address_subtitle.jq_tooltip ::text').get(),
    #         'stars': '5',
    #         # 'price': ,
    #         'ratings': response.css('div.hp_review_score_entry > a > div > div > div > div > div.b5cd09854e.d10a6220b4 ::text').get(),
    #         'number of reviewers': response.xpath('//*[@id="guest-featured_reviews__horizontal-block"]/div/div[1]/a/div/div/div/div/div[2]/span[2]/text()')[0].get(),
    #         'facilities': response.css('div.bui-grid__column.bui-grid__column-12.js-k2-hp--block.k2-hp--popular_facilities > div> div.important_facility ::text').getall(),
    #         'description': response.css('#property_description_content > p:nth-child(2) ::text').get(),
    #         # 'nearby_places':
    #     }

    # def parse(self, response):
    #     yield {
    #         'city': 'Hà Nội',
    #         'url': response.url,
    #         'name': response.xpath('//*[@id="app-layer-base"]/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[1]/h1/text()').get(),
    #         'address': response.css('span.HeaderCerebrum__Address ::text').get(),
    #         # 'stars': '5',
    #         # 'price': ,
    #         'ratings': response.css('div.uitk-text.uitk-type-900.uitk-type-regular.uitk-text-default-theme span ::text').get(),
    #         'number of reviewers': response.css('div.uitk-layout-flex.uitk-layout-flex-flex-direction-column.all-t-padding-one div.uitk-layout-flex button ::text').get(),
    #         'facilities': response.css('div.Box-sc-kv6pi1-0.eqoTHM > p::text').getall(),
    #         'description': response.css('div.Box-sc-kv6pi1-0.bhFfcp > p ::text').get(),
    #         # 'nearby_places':
    #     }
    # pass
