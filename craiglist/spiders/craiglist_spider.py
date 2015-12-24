import scrapy
from scrapy.selector import HtmlXPathSelector
from craiglist.items import CraiglistItem

class DmozSpider(scrapy.Spider):


    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraiglistItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items

#        titles = hxs.select("//span[@class='pl']")
#        for titles in titles:
#            title = titles.select("a/text()").extract()
#            link = titles.select("a/@href").extract()
#            print title, link



#    name = "dmoz"
#    allowed_domains = ["dmoz.org"]
#    start_urls = [
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#    ]
#
#    def parse(self, response):
#        filename = response.url.split("/")[-2] + '.html'
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#
#        for sel in response.xpath('//ul/li'):
#            title = sel.xpath('a/text()').extract()
#            link = sel.xpath('a/@href').extract()
#            desc = sel.xpath('text()').extract()
#            print title, link, desc
