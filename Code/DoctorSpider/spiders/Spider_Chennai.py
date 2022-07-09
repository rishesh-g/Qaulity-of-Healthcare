import scrapy
from ..items import DoctorspiderItem

class doctorSpider(scrapy.Spider):
    name = 'doctors1'
    page_num = 2
    start_urls = ['https://www.practo.com/kolkata/doctors?page=1']

    def parse(self, response):
        doctors = response.xpath("//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'info-section', ' ' ))]")
        for doctor in doctors:
            link = doctor.css("a::attr(href)").extract_first()
            req = 'https://www.practo.com' + link

            yield scrapy.Request(req,callback=self.parse_page)

        next_page = 'https://www.practo.com/kolkata/doctors?page=' + str(doctorSpider.page_num)
        if doctorSpider.page_num <= 1:
            doctorSpider.page_num = doctorSpider.page_num + 1
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        item = DoctorspiderItem()
        item['Name'] = response.css(".u-bold.u-d-inlineblock::text").extract_first()
        item['City'] = response.css(".u-d-inlineblock:nth-child(2) .u-smallest-font .u-c-pointer::text").extract_first()
        item['Specialization'] = response.css(".u-d-inlineblock:nth-child(3) .u-c-pointer::text").extract_first()
        item['Degree'] = response.css(".c-profile--qualification p::text").extract_first()
        item['Experience'] = response.css(".c-profile__details span+ .u-d-inlineblock::text").extract_first()
        item['Fees'] = response.css(".u-no-margin--top span::text")[3].extract()
        item['Rating'] = response.css(".common__star-rating__value::text").extract()
        item['Address'] = response.css("h2 .c-profile--clinic__name::text").extract()
        item['Feedback'] = response.css(".u-d-inline::text").extract()

        return item




import scrapy
from ..items import DoctorspiderItem

class doctorSpider(scrapy.Spider):
    name = 'chennai'
    page_num = 2
    start_urls = ['https://www.practo.com/chennai/doctors?page=1']

    def parse(self, response):
        doctors = response.xpath("//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'info-section', ' ' ))]")
        for doctor in doctors:
            link = doctor.css("a::attr(href)").extract_first()
            req = 'https://www.practo.com' + link

            yield scrapy.Request(req,callback=self.parse_page)

        next_page = 'https://www.practo.com/chennai/doctors?page=' + str(doctorSpider.page_num)
        if doctorSpider.page_num <= 632:
            doctorSpider.page_num = doctorSpider.page_num + 1
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        item = DoctorspiderItem()
        item['Name'] = response.css(".u-bold.u-d-inlineblock::text").extract_first()
        item['City'] = response.css(".u-d-inlineblock:nth-child(2) .u-smallest-font .u-c-pointer::text").extract_first()
        item['Specialization'] = response.css(".u-d-inlineblock:nth-child(3) .u-c-pointer::text").extract_first()
        item['Degree'] = response.css(".c-profile--qualification p::text").extract_first()
        item['Experience'] = response.css(".c-profile__details span+ .u-d-inlineblock::text").extract_first()
        item['Fees'] = response.css(".u-no-margin--top span::text")[3].extract()
        item['Rating'] = response.css(".common__star-rating__value::text").extract()
        item['Address'] = response.css("h2 .c-profile--clinic__name::text").extract()
        item['Feedback'] = response.css(".feedback__content.u-large-font::text").extract()

        return item




