# -*- coding: utf-8 -*-

from currency.items import ExchangeRateItem
import scrapy
import unicodedata


class ExchangeRateSpider (scrapy.Spider):
    name = 'exchange_rate'
    allowed_domains = ['bot.com.tw']
    start_urls = ['https://rate.bot.com.tw/xrt?Lang=zh-TW']

    def parse(self, response):
        yield scrapy.Request('https://rate.bot.com.tw/xrt?Lang=zh-TW', callback=self.parse_exchange_rate)

    def parse_exchange_rate(self, response):
        item = ExchangeRateItem()
        target = response.css('table[title="牌告匯率"]>tbody>tr')

        for tag in target:
            try:
                item['currency'] = tag.css(
                    'td[data-table="幣別"] div.visible-phone.print_hide::text')[0].extract().strip()
                item['cash_buy'] = tag.css(
                    'td[data-table="本行現金買入"]::text')[0].extract().strip()
                item['cash_sell'] = tag.css(
                    'td[data-table="本行現金賣出"]::text')[0].extract().strip()
                item['account_buy'] = tag.css(
                    'td[data-table="本行即期買入"]::text')[0].extract().strip()
                item['account_sell'] = tag.css(
                    'td[data-table="本行即期賣出"]::text')[0].extract().strip()

                yield item

            except IndexError:
                pass
            continue
