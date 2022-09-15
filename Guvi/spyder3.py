import pandas
import scrapy
import scrapy_playwright

class Spyder3Spider(scrapy.Spider):
    name = "spyd3"
    def start_requests(self):
            url = "https://www.guvi.in/courses"    
            yield scrapy.Request(url, meta={'playwright': True})
    def parse(self, response):
        for link in response.css("div#data-science-micro-degree").css("a::attr(href)"):
            yield response.follow(link.get(), callback=self.parser_contents1)
        for link in response.xpath("//*[@id='premiumLib']//div//a/@href"):
            yield scrapy.Request(response.urljoin(link.get()), meta={'playwright':True}, callback=self.parser_contents1)
    def parser_contents1(self, response):
        link = response.request.url
        name = response.xpath("//*[@id='courses-watch']/section[1]/div[1]/div[2]/h1//text()").get()
        desc = response.xpath("//*[@id='about_description']/text()").get()
        desc = "<p>" + str(desc) + "</p>"
        #course_vid = response.xpath("//*[@id='course-video']//@src").get()
        author = response.xpath("//*[@id='author']/div[1]/div/div[1]/h4/text()").get()
        c_outcome = response.xpath("//*[@id='achieve_text']//li//span//text()").getall()
        c_outcome = "| ".join(c_outcome)
        duration = response.xpath("//*[@id='aside_']/aside/div[1]/div[2]/text()").get()
        curr_price = response.xpath("//*[@id='aside_']/aside/div[5]/div[2]/div/div[1]//text()").get()
        price = response.xpath("//*[@id='aside_']/aside/div[5]/div[2]/div/div[2]/del//text()").get()
        lang = response.xpath("//*[@id='aside_']/aside/div[2]/div[2]/text()").get()
        review = response.xpath("//*[@id='aside_']/aside/div[4]/div[2]/text()").get()
        st_enr = response.xpath("//*[@id='aside_']/aside/div[3]/div[2]/text()").get()
        ab_auth = response.xpath("//*[@id='author']/div[2]/text()").get()
        ab_auth = "<p>" + str(ab_auth) + "</p>"
        prereq = response.xpath("//*[@id='requirements']/div/span[2]/text()").getall()
        prereq = "| ".join(prereq)
        module = response.css(".course_content_main").css(".accordion-button div::text").getall()
        module.pop(0)
        print(len(module))
        submod = list()
        for i in range(1,len(module)+1):
            submod.append(response.xpath(f"/html/body/main/section[1]/div[2]/div/div[{i}]").css(".lessonName::text").getall())
        faq_q = response.css(".col-lg-8").css(".accordion-button div::text").getall()
        faq_a = response.css(".col-lg-8").css(".faQ_body::text").getall()
        #print(len(submod))
        #print(len(faq_a))
        #print(len(faq_q))
        faq_q = "| ".join(faq_q)
        faq_a = "| ".join(faq_a)
        modulenum = 1
        modlist = list()
        for i in range(len(module)):
            mod = f"<p><strong>Module{modulenum}. {module[i]}</strong>"
            modlist.append(mod)
            try:
                submodnum = 1
                if submod[i] is not None:
                    for j in submod[i]:
                        submodule = f"<br>{submodnum}. {j}"
                        modlist.append(submodule)
                        submodnum += 1
                else:
                    pass
            except:
                pass
            modulenum +=1
            modlist.append("</p>")
        content = "".join(modlist)


        yield {
            'Course Name': name,
            'Course Link': link,
            'Description': desc,
            'Author': author,
            #'vid_link': course_vid,
            'Author description': ab_auth,
            'Course Outcomes': c_outcome,
            'Duration': duration,
            'Current Price': curr_price,
            'Price': price,
            'Who can take this course': prereq,
            'Language': lang,
            'Review': review,
            'Students Enrolled': st_enr,
            #'Modules': module,
            #'Sub modules': submod,
            'Faq_q': faq_q,
            'Faq_a': faq_a,
            'Syllabus': content
        }
        