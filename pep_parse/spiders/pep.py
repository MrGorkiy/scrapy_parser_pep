import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.xpath('//*[@id="numerical-index"]')
        tbody = all_pep.css('tbody')
        href_pep = tbody.css('a[href^="/pep-"]')
        for pep_url in href_pep:
            yield response.follow(pep_url,
                                  callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
