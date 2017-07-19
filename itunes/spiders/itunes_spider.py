import scrapy

from scrapy.spiders import XMLFeedSpider

class ItunesSpider(XMLFeedSpider):
    name = "itunes"
    start_urls = ('https://rss.itunes.apple.com/api/v1/us/books/top-free/100/explicit/xml','https://rss.itunes.apple.com/api/v1/us/books/top-paid/100/explicit/xml','https://rss.itunes.apple.com/api/v1/us/audiobooks/top-audiobooks/100/explicit/xml','https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/100/explicit/xml','https://rss.itunes.apple.com/api/v1/us/itunes-u/top-itunes-u-collection/100/explicit/xml','https://rss.itunes.apple.com/api/v1/us/itunes-u/top-itunes-u-courses/100/explicit/xml')
    itertag = 'item'
    
    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s',self.itertag, ''.join(node.extract()))
        
        item = {}
        item['Title'] = node.xpath('title/text()',).extract_first()
        item['Description'] = node.xpath('description/text()',).extract_first()
        item['Creator'] = node.xpath('category/text()').extract_first()
        item['URL'] = node.xpath('link/text()').extract_first()
        item['Type'] = node.xpath('category/text()').extract()[1]
        return item