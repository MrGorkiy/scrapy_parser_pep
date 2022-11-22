from scrapy import signals


class PepParseBase:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseSpiderMiddleware(PepParseBase):
    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r


class PepParseDownloaderMiddleware(PepParseBase):
    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response
