# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorspiderItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    City = scrapy.Field()
    Specialization = scrapy.Field()
    Degree = scrapy.Field()
    Experience = scrapy.Field()
    Fees = scrapy.Field()
    Rating = scrapy.Field()
    Address = scrapy.Field()
    Feedback = scrapy.Field()


    pass
