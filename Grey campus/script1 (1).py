import scrapy
from scrapy.crawler import CrawlerProcess


class Spider123(scrapy.Spider):
    name = 'x2'

    def start_requests(self):
        yield scrapy.Request('https://www.greycampus.com/project-management')

    def parse(self, response):
        link = response.request.url
        if (link!="https://www.greycampus.com/project-management") or (link != 'https://www.greycampus.com/enterprise'):
            deli = '|'
            res1 = ''
            res2 = ''
            res3 = ''
            res4 = ''

            # name of course
            if response.xpath("//*[@id='top']/text()").extract():
                x = response.xpath("//*[@id='top']/text()").extract()
            elif response.xpath(
                    "/html/body/div[1]/main/div/div/div/div/div[1]/div/div/div[1]/div/div/div/span/h1/span/strong"):
                x = response.xpath(
                    "/html/body/div[1]/main/div/div/div/div/div[1]/div/div/div[1]/div/div/div/span/h1/span/strong/text()").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1/strong/span/text()").extract():
                x = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1/strong/span/text()").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1/span/text()").extract():
                x = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1/span/text()").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[1]/div/h1"):
                x = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[1]/div/h1/text()").extract()
            elif response.css("h1"):
                x = response.css("h1::text").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1"):
                x = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/h1/text()").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[1]/h1"):
                x = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[1]/h1/text()").extract()
            else:
                x = "n/a"
            # short description
            if response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/p/span/text()").extract():
                y = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/p/span/text()").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/p/text()").extract():
                y = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/p/text()").extract()
            elif response.css(".dnd_area-column-1-vertical-alignment").extract():
                y = response.css("div span p::text").extract()
            elif response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[2]/p[1]/text()"):
                y = response.xpath("//*[@id='hs_cos_wrapper_dnd_area-module-2_']/div[2]/p[1]/text()").extract()
            elif response.xpath("//*[@id='Second_2']/div/ul/li/span"):
                y = response.xpath("//*[@id='Second_2']/div/ul/li/span/text()").extract()
            else:
                y = "n/a"

            for ele in y:
                res1 = res1 + str(ele)
            if y:
                s_descr = "<p>" + str(res1) + "</p>"
            elif not y:
                s_descr = y
            # program Outcome
            # course curriculum1
            y = response.css("div#curriculum.accordion")
            y2 = response.css(".dnd_area-row-3-background-color")
            if y:
                for links in y:
                    z = links.css(
                        "button.accordion-button.bg-dark.py-4.border-bottom.text-white.collapsed::text").extract()
                    if z:
                        z = z
                    else:
                        z = "n/a"
            if not y:
                if y2:
                    for links in y2:
                        z = links.css(
                            "button.accordion-button.bg-dark.py-4.border-bottom.text-white.collapsed::text").extract()
                else:
                    z = 'n/a'
            if z != 'n/a':
                for i in range(len(z)):
                    z[i] = z[i].strip()
                    z[i] = z[i].replace("Lesson", "")
                    z[i] = ''.join(i for i in z[i] if not i.isdigit())
                    z[i] = z[i].replace(":", "")
                    z[i] = z[i].replace(".", "")
                    z[i] = z[i].lstrip(" ")
            # long descvription
            ld = response.css(".dnd_area-row-1-margin")
            res2 = ''
            descr = list()
            if ld:
                if ld.css("ul li"):
                    for i in ld.css("ul li"):
                        descr.append(i.css('ul li::text').extract())
                elif ld.css("p"):
                    for i in ld.css("p"):
                        descr.append(i.css("p::text").extract())
                elif ld.css("p span"):
                    for i in ld.css("p span"):
                        descr.append(i.css("p span::text").extract())
            if not ld:
                ld1 = response.css(".dnd_area-row-0-background-image")
                if ld1.css("p"):
                    for i in ld1.css("p"):
                        descr.append(i.css("p::text").extract())
                if ld1.css("p span"):
                    for i in ld1.css("p span"):
                        descr.append(i.css("p span::text").extract())
                if ld1.css("span"):
                    for i in ld1.css("span"):
                        descr.append(i.css("span::text").extract())

            for i in descr:
                for j in i:
                    res2 = res2 + str(j)
            res2 = res2.strip()
            res2 = "<p>" + res2 + "</p>"
            # student reviews
            sr = response.css(".glide__track")
            t = list()
            if not sr:
                t.append('N/A')
            elif sr:
                sr1 = sr.css(".fw-bold::text").extract()
                sr1 = list(set(sr1))
                if sr.css("p"):
                    srr = sr.css("p::text").extract()
                if sr.css("span"):
                    srr = sr.css("span::text").extract()
                srr = list(set(srr))
                if len(sr1) == len(srr):
                    for i in range(len(srr)):
                        if sr1 and srr:
                            t.append(str(sr1[i]) + deli + str(srr[i]) + deli)
                elif len(sr1) == 0:
                    t.append("n/a")

            modlist = list()
            modulenum = 1
            for i in range(len(z)):
                module = f"<p><strong>Module{modulenum}. {z[i]}</strong>"
                modlist.append(module)
                modulenum += 1
                modlist.append("</p>")
            content = "".join(modlist)

            yield {
                'Name of Course': x,
                'Course Link': link,
                'Short Description': s_descr,
                'Long Description': res2,
                'Course Outcomes': z,
                'Syllabus': content,
                'Reviews': t
            }
        for i in response.xpath("//*[@id='hs_cos_wrapper_All_courses']/div/ul/li/div/div/ul/li/a/@href"):
            url = "https://www.greycampus.com" + str(i.extract())
            yield(scrapy.Request(url, callback=self.parse))


process = CrawlerProcess(settings={
    'FEED_URI': 'dataGreyCampus2.csv',
    'FEED_FORMAT': 'csv'

})
process.crawl(Spider123)
process.start()
