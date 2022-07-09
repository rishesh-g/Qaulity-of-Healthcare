import scrapy
from ..items import DoctorspiderItem

class doctorSpider(scrapy.Spider):
    name = 'doctors'
    page_num = 2
    start_urls = [
        'https://www.practo.com/kolkata/doctors?page=1',
        'https://www.practo.com/kolkata/doctors?page=2'

    ]

    def parse(self, response):
        item = DoctorspiderItem()
        doctors = response.xpath("//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'info-section', ' ' ))]")
        print(len(doctors))


        for doctor in doctors :
            names = doctor.xpath(".//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'doctor-name', ' ' ))]/text()").extract_first()
            specialization = doctor.xpath(".//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'u-d-inline', ' ' ))]//span/text()").extract_first()
            exp = doctor.xpath(".//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'uv2-spacer--xs-top', ' ' ))]//div/text()").extract_first()
            fee = doctor.xpath(".//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'uv2-spacer--xs-top', ' ' ))]//span//span/text()").extract_first()
            link = doctor.css("a::attr(href)").extract_first()
            req = scrapy.Request('https://www.practo.com' + link)

            item['name'] = names
            item['specialization'] = specialization
            item['experience'] = exp
            item['fees'] = fee
            item['link'] = link


            yield item






