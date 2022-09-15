import scrapy
from ..items import DatatrainedItem

class firstscrappy(scrapy.Spider):
    name = "scrap"
    start_urls = [
        "https://www.datatrained.com/"
    ]

    def parse(self, response):
        for link in response.css("div#data-science-micro-degree").css("a::attr(href)"):
            yield response.follow(link.get(), callback=self.parser_contents1)
        for link in response.css("div#software-development-micro-degree").css("a::attr(href)"):
            yield response.follow(link.get(), callback=self.parser_contents2)
        for link in response.css("div#management-micro-degree").css("a::attr(href)"):
            yield response.follow(link.get(), callback=self.parser_contents3)

    def parser_contents1(self, response):
        items = DatatrainedItem()

        title = []
        for i in response.css("div.cont-box"):
            if i.css("h2") is not None:
                title.append(i.css("h2::text").extract_first())
        for j in response.css("div.cont-box"):
            if j.css("h4") is not None:
                title.append(j.css("h4::text").extract_first())
        filtered_list = list(filter(None, title))
        title = filtered_list
        #title = response.css("div.cont-box").css("h2::text").extract_first()

        desc = response.css("div.place-heading.top-heading").css("p").extract()
        try:
            cover_video = response.css("div.program-vedio").css("iframe").attrib["src"]
        except:
            pass
        cover_img = response.css("div.pg-program-vedio").attrib["style"].split()[1].replace("url", "").replace(";", "")

        content_module = []
        for i in response.css("div.syllabus-newbox"):
            if i.css("h4") is not None:
                content_module.append(i.css("h4::text").extract_first())
        for j in response.css("div.syllabus-newbox"):
            if j.css("span") is not None:
                content_module.append(j.css("span.module-heading::text").extract_first())
        for k in response.css("div.card-body"):
            if k.css("span") is not None:
                content_module.append(k.css("span::text").extract_first())
        filtered_list1_0 = list(filter(None, content_module))
        content_module = "| ".join(filtered_list1_0)

        total_duration = response.css("div.cont-box").css("li::text")[4].extract()
        course_start_date = response.css("div.banner-detail").css("p::text")[2].extract().strip()
        course_duration = response.css("div.banner-detail").css("p::text")[1].extract().strip()
        display_price = response.css("div.cont-box").css("li.time-pg").css("span::text").extract_first()

        instructor = []
        for i in response.css("div.row.justify-content-center").css("div.col-lg-4.col-md-6.col-12"):
           if i.css("h5") is not None:
               instructor.append(i.css("h5::text").extract_first())
           if i.css("h3") is not None:
               instructor.append(i.css("h3::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
           if j.css("h5") is not None:
               instructor.append(j.css("h5::text").extract_first())
        filtered_list1 = list(filter(None, instructor))
        instructor = filtered_list1[:6]
        instructor = "| ".join(instructor)

        inst_desig = []
        for i in response.css("div.col-lg-4.col-md-6.col-12"):
            if i.css("span") is not None:
                inst_desig.append(i.css("span::text").extract_first())
            elif i.css("h6") is not None:
                inst_desig.append(i.css("h6::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("h6") is not None:
                inst_desig.append(j.css("h6::text").extract_first())
        filtered_list2 = list(filter(None, inst_desig))
        inst_desig = filtered_list2[1:7]
        inst_desig = "| ".join(inst_desig)
        #inst_desig = [i.css("span::text").extract_first() for i in response.css("div.col-lg-4.col-md-6.col-12")][4:8]

        inst_bio = []
        for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12"):
            if i.css("p") is not None:
                inst_bio.append(i.css("p::text").extract_first().strip())
        for j in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("p") is not None:
                inst_bio.append(j.css("p::text").extract_first().strip())
        inst_bio = "| ".join(inst_bio)
        #inst_bio = [i.css("p::text").extract_first() for i in response.css("div.col-lg-4.col-md-6.col-12")][4:8]

        inst_img = []
        for i in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12")]:
            try:
                if i.attrib["src"] is not None:
                    inst_img.append(i.attrib["src"])
            except:
                pass
        for j in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ")]:
            try:
                if j.attrib["src"] is not None:
                    inst_img.append(j.attrib["src"])
            except:
                pass
        inst_img = "| ".join(inst_img)
        #inst_img = [j.attrib["src"] for j in[i.css("img") for i in response.css("div.col-lg-4.col-md-6.col-12")][:4]]
        try:
            avg_sal_hike = response.css("div.col-lg-4.col-md-12.flex").css("img").attrib["alt"]
        except:
            avg_sal_hike = None
        try:
            high_sal = response.css("div.col-lg-4.col-md-12.flex").css("img")[1].attrib["alt"]
        except:
            high_sal = None

        reviewer_names = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("span.name") is not None:
                reviewer_names.append(i.css("span.name::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3") or response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if j.css("h5") is not None:
                reviewer_names.append(j.css("h5::text").extract_first())
        filtered_list3 = list(filter(None, reviewer_names))
        reviewer_names = "| ".join(filtered_list3)

        reviewer_photos = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("img") is not None:
                reviewer_photos.append(i.css("img").attrib["src"])
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("img") is not None:
                reviewer_photos.append(j.css("img").attrib["src"])
        reviewer_photos = "| ".join(reviewer_photos)
        #reviewer_photos = [i.css("img").attrib["src"] for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3")]

        reviews = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("p") is not None:
                reviews.append(i.css("p::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("p") is not None:
                reviews.append(j.css("p::text").extract_first())
        reviews = "| ".join(reviews)
        #reviews = [i.css("p::text").extract_first() for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3")]

        try:
            faq_questions = [j.extract().strip().replace("\r\n", "").replace("                            ", "").replace("                           ", "") for j in [i.css("h3::text") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_questions = "|".join(faq_questions)
            faq_answers = [j.css("p::text").extract_first().strip().replace("\r\n","").replace("                                 ","") for j in [i.css("div.card") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_answers = "|".join(faq_answers)
        except:
            faq_questions = None
            faq_answers = None

        modules = [j.extract() for j in response.css("div.accordion.md-accordion").css("h5.mb-0::text")]
        sub_mod = [i.css("span::text").extract() for i in response.css("div.col-lg-12")][:-10]
        sub_mod = sub_mod[3:]
        modlist = list()
        # print(len(sub_mod))
        modulenum = 1
        for i in range(len(modules)):
            module = f"<p><strong>Module {modulenum}: {modules[i]}</strong>"
            modlist.append(module)
            # print(module)
            try:
                submodnum = 1
                for j in sub_mod[i]:
                    submodule = f"<br>{submodnum}. {j}"
                    modlist.append(submodule)
                    submodnum += 1
            except:
                pass

            modulenum += 1
            modlist.append('</p>')

        contents = "".join(modlist)
        #print(contents)

        items["title"] = title
        items["desc"] = desc
        items["contents"] = contents
        items["cover_video"] = cover_video
        items["cover_img"] = cover_img
        items["content_module"] = content_module
        items["total_duration"] = total_duration
        items["course_start_date"] = course_start_date
        items["course_duration"] = course_duration
        items["display_price"] = display_price
        items["instructor"] = instructor
        items["inst_desig"] = inst_desig
        items["inst_img"] = inst_img
        items["inst_bio"] = inst_bio
        items["avg_sal_hike"] = avg_sal_hike
        items["high_sal"] = high_sal
        items["reviewer_names"] = reviewer_names
        items["reviewer_photos"] = reviewer_photos
        items["reviews"] = reviews
        items["faq_questions"] = faq_questions
        items["faq_answers"] = faq_answers

        yield items

    def parser_contents2(self, response):
        items = DatatrainedItem()

        title = []
        for i in response.css("div.cont-box"):
            if i.css("h2") is not None:
                title.append(i.css("h2::text").extract_first())
        for j in response.css("div.cont-box"):
            if j.css("h4") is not None:
                title.append(j.css("h4::text").extract_first())
        filtered_list = list(filter(None, title))
        title = filtered_list

        desc = response.css("div.place-heading.top-heading").css("p").extract()
        cover_video = response.css("div.program-vedio").css("iframe").attrib["src"]
        cover_img = response.css("div.pg-program-vedio").attrib["style"].split()[1].replace("url", "").replace(";", "")

        content_module = []
        for i in response.css("div.syllabus-newbox"):
            if i.css("h4") is not None:
                content_module.append(i.css("h4::text").extract_first())
        for j in response.css("div.syllabus-newbox"):
            if j.css("span") is not None:
                content_module.append(j.css("span.module-heading::text").extract_first())
        for k in response.css("div.card-body"):
            if k.css("span") is not None:
                content_module.append(k.css("span::text").extract_first())
        filtered_list1_0 = list(filter(None, content_module))
        content_module = "| ".join(filtered_list1_0)
        total_duration = response.css("div.cont-box").css("li::text")[4].extract()
        course_start_date = response.css("div.banner-detail").css("p::text")[3].extract().strip()
        course_duration = response.css("div.banner-detail").css("p::text")[2].extract().strip()
        display_price = response.css("div.cont-box").css("li.time-pg").css("span::text").extract_first()
        instructor = []
        for i in response.css("div.row.justify-content-center").css("div.col-lg-4.col-md-6.col-12"):
            if i.css("h5") is not None:
                instructor.append(i.css("h5::text").extract_first())
            if i.css("h3") is not None:
                instructor.append(i.css("h3::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("h5") is not None:
                instructor.append(j.css("h5::text").extract_first())
        for k in response.css("div.row.justify-content-center").css("div.col-lg-4.col-md-6"):
            if k.css("h3") is not None:
                instructor.append(k.css("h3::text").extract_first())
        filtered_list1 = list(filter(None, instructor))
        instructor = filtered_list1[:5]
        instructor = "| ".join(instructor)

        inst_desig = []
        for i in response.css("div.col-lg-4.col-md-6.col-12"):
            if i.css("span") is not None:
                inst_desig.append(i.css("span::text").extract_first())
            elif i.css("h6") is not None:
                inst_desig.append(i.css("h6::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("h6") is not None:
                inst_desig.append(j.css("h6::text").extract_first())
        for k in response.css("div.row.justify-content-center").css("div.col-lg-4.col-md-6"):
            if k.css("span") is not None:
                inst_desig.append(k.css("span::text").extract_first())
        filtered_list2 = list(filter(None, inst_desig))
        inst_desig = filtered_list2[1:7]
        inst_desig = "| ".join(inst_desig)
        # inst_desig = [i.css("span::text").extract_first() for i in response.css("div.col-lg-4.col-md-6.col-12")][4:8]

        inst_bio = []
        for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12"):
            if i.css("p") is not None:
                inst_bio.append(i.css("p::text").extract_first().strip())
        for j in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css(
                "section.instructors").css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("p") is not None:
                inst_bio.append(j.css("p::text").extract_first().strip())
        inst_bio = "| ".join(inst_bio)

        inst_img = []
        for i in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12")]:
            try:
                if i.attrib["src"] is not None:
                    inst_img.append(i.attrib["src"])
            except:
                pass
        for j in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ")]:
            try:
                if j.attrib["src"] is not None:
                    inst_img.append(j.attrib["src"])
            except:
                pass
        inst_img = "| ".join(inst_img)
        try:
            avg_sal_hike = response.css("div.col-lg-4.col-md-12.flex").css("img").attrib["alt"]
        except:
            avg_sal_hike = None
        try:
            high_sal = response.css("div.col-lg-4.col-md-12.flex").css("img")[1].attrib["alt"]
        except:
            high_sal = None

        reviewer_names = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3") or response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if i.css("span.name") is not None:
                reviewer_names.append(i.css("span.name::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3") or response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if j.css("h5") is not None:
                reviewer_names.append(j.css("h5::text").extract_first())
        for k in response.css("div.col-lg-6.col-md-6.col-12.my-3"):
            if k.css("span") is not None:
                reviewer_names.append(k.css("span.name::text").extract_first())

        filtered_list3 = list(filter(None, reviewer_names))
        reviewer_names = "| ".join(filtered_list3)

        reviewer_photos = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("img") is not None:
                reviewer_photos.append(i.css("img").attrib["src"])
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("img") is not None:
                reviewer_photos.append(j.css("img").attrib["src"])
        for k in response.css("div.col-lg-6.col-md-6.col-12.my-3"):
            if k.css("img") is not None:
                reviewer_photos.append(k.css("img").attrib["src"])
        reviewer_photos = "| ".join(reviewer_photos)
        # reviewer_photos = [i.css("img").attrib["src"] for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3")]

        reviews = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("p") is not None:
                reviews.append(i.css("p::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("p") is not None:
                reviews.append(j.css("p::text").extract_first())
        for k in response.css("div.col-lg-6.col-md-6.col-12.my-3"):
            if k.css("p") is not None:
                reviews.append(k.css("p::text").extract_first())
        reviews = "| ".join(reviews)
        try:
            faq_questions = [j.extract().strip().replace("\r\n", "").replace("                            ", "").replace("                           ", "") for j in [i.css("h3::text") or i.css("h5::text") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_questions = "|".join(faq_questions)
            faq_answers = [j.css("p::text").extract_first().strip().replace("\r\n","").replace("                                 ","") for j in [i.css("div.card") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_answers = "|".join(faq_answers)
        except:
            faq_questions = None
            faq_answers = None

        module = []
        for i in response.css("div.accordion.md-accordion").css("h4.mb-0::text").extract():
            if i is not None:
                module.append(i.replace("                           ","").replace("\n",""))
        for j in response.css("div.accordion.md-accordion").css("h5.mb-0::text").extract():
            if j is not None:
                module.append(j.replace("                           ","").replace("\n",""))
        modules = []
        for ele in module:
            if ele.strip():
                modules.append(ele)
        modules = modules[:3]
        #modules = [j.extract() for j in response.css("div.accordion.md-accordion").css("h4.mb-0::text")]

        sub_mod = [i for i in response.css("div.accordion.md-accordion").css("li::text").extract()][:-20]
        modlist = list()
        print(sub_mod)
        print(modules)
        modulenum = 1
        for i in range(len(modules)):
            module = f"<p><strong>Module {modulenum}: {modules[i]}</strong>"
            modlist.append(module)
            # print(module)
            try:
                submodnum = 1
                for j in sub_mod:
                    submodule = f"<br>{submodnum}. {j}"
                    modlist.append(submodule)
                    submodnum += 1
            except:
                pass

            modulenum += 1
            modlist.append('</p>')

        contents = "".join(modlist)

        items["title"] = title
        items["desc"] = desc
        items["contents"] = contents
        items["cover_video"] = cover_video
        items["cover_img"] = cover_img
        items["content_module"] = content_module
        items["total_duration"] = total_duration
        items["course_start_date"] = course_start_date
        items["course_duration"] = course_duration
        items["display_price"] = display_price
        items["instructor"] = instructor
        items["inst_desig"] = inst_desig
        items["inst_img"] = inst_img
        items["inst_bio"] = inst_bio
        items["avg_sal_hike"] = avg_sal_hike
        items["high_sal"] = high_sal
        items["reviewer_names"] = reviewer_names
        items["reviewer_photos"] = reviewer_photos
        items["reviews"] = reviews
        items["faq_questions"] = faq_questions
        items["faq_answers"] = faq_answers

        yield items

    def parser_contents3(self, response):
        items = DatatrainedItem()

        title = []
        for i in response.css("div.cont-box"):
            if i.css("h2") is not None:
                title.append(i.css("h2::text").extract_first())
        for j in response.css("div.cont-box"):
            if j.css("h4") is not None:
                title.append(j.css("h4::text").extract_first())
        filtered_list = list(filter(None, title))
        title = filtered_list
        #title = response.css("div.cont-box").css("h2::text").extract_first()

        desc = response.css("div.place-heading.top-heading").css("p").extract()
        try:
            cover_video = response.css("div.program-vedio").css("iframe").attrib["src"]
        except:
            pass
        cover_img = response.css("div.pg-program-vedio").attrib["style"].split()[1].replace("url", "").replace(";", "")

        content_module = []
        for i in response.css("div.syllabus-newbox"):
            if i.css("h4") is not None:
                content_module.append(i.css("h4::text").extract_first())
        for j in response.css("div.syllabus-newbox"):
            if j.css("span") is not None:
                content_module.append(j.css("span.module-heading::text").extract_first())
        for k in response.css("div.card-body"):
            if k.css("span") is not None:
                content_module.append(k.css("span::text").extract_first())
        filtered_list1_0 = list(filter(None, content_module))
        content_module = "| ".join(filtered_list1_0)

        total_duration = response.css("div.cont-box").css("li::text")[4].extract()
        course_start_date = response.css("div.banner-detail").css("p::text")[3].extract().strip()
        course_duration = response.css("div.banner-detail").css("p::text")[2].extract().strip()
        display_price = response.css("div.cont-box").css("li.time-pg").css("span::text").extract_first()

        instructor = []
        for i in response.css("div.row.justify-content-center").css("div.col-lg-4.col-md-6.col-12"):
           if i.css("h5") is not None:
               instructor.append(i.css("h5::text").extract_first())
           if i.css("h3") is not None:
               instructor.append(i.css("h3::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
           if j.css("h5") is not None:
               instructor.append(j.css("h5::text").extract_first())
        filtered_list1 = list(filter(None, instructor))
        instructor = filtered_list1[:5]
        instructor = "| ".join(instructor)

        inst_desig = []
        for i in response.css("div.col-lg-4.col-md-6.col-12"):
            if i.css("span") is not None:
                inst_desig.append(i.css("span::text").extract_first())
            elif i.css("h6") is not None:
                inst_desig.append(i.css("h6::text").extract_first())
        for j in response.css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("h6") is not None:
                inst_desig.append(j.css("h6::text").extract_first())
        filtered_list2 = list(filter(None, inst_desig))
        inst_desig = filtered_list2[1:7]
        inst_desig = "| ".join(inst_desig)
        #inst_desig = [i.css("span::text").extract_first() for i in response.css("div.col-lg-4.col-md-6.col-12")][4:8]

        inst_bio = []
        for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12"):
            if i.css("p") is not None:
                inst_bio.append(i.css("p::text").extract_first().strip())
        for j in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ") or response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12"):
            if j.css("p") is not None:
                inst_bio.append(j.css("p::text").extract_first().strip())
        inst_bio = "| ".join(inst_bio)
        #inst_bio = [i.css("p::text").extract_first() for i in response.css("div.col-lg-4.col-md-6.col-12")][4:8]

        inst_img = []
        for i in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-12")]:
            try:
                if i.attrib["src"] is not None:
                    inst_img.append(i.attrib["src"])
            except:
                pass
        for j in [i.css("img") for i in response.css("section.instructors").css("div.col-lg-4.col-md-6.col-sm-12 ")]:
            try:
                if j.attrib["src"] is not None:
                    inst_img.append(j.attrib["src"])
            except:
                pass
        inst_img = "| ".join(inst_img)
        #inst_img = [j.attrib["src"] for j in[i.css("img") for i in response.css("div.col-lg-4.col-md-6.col-12")][:4]]
        try:
            avg_sal_hike = response.css("div.col-lg-4.col-md-12.flex").css("img").attrib["alt"]
        except:
            avg_sal_hike = None
        try:
            high_sal = response.css("div.col-lg-4.col-md-12.flex").css("img")[1].attrib["alt"]
        except:
            high_sal = None

        reviewer_names = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("span.name") is not None:
                reviewer_names.append(i.css("span.name::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3") or response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if j.css("h5") is not None:
                reviewer_names.append(j.css("h5::text").extract_first())
        filtered_list3 = list(filter(None, reviewer_names))
        reviewer_names = "| ".join(filtered_list3)

        reviewer_photos = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("img") is not None:
                reviewer_photos.append(i.css("img").attrib["src"])
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("img") is not None:
                reviewer_photos.append(j.css("img").attrib["src"])
        reviewer_photos = "| ".join(reviewer_photos)
        #reviewer_photos = [i.css("img").attrib["src"] for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3")]

        reviews = []
        for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3"):
            if i.css("p") is not None:
                reviews.append(i.css("p::text").extract_first())
        for j in response.css("div.col-xl-4.col-lg-6.col-md-6.mt-3.mb-3"):
            if j.css("p") is not None:
                reviews.append(j.css("p::text").extract_first())
        reviews = "| ".join(reviews)
        #reviews = [i.css("p::text").extract_first() for i in response.css("div.col-xl-4.col-lg-6.col-md-6.col-12.my-3")]

        try:
            faq_questions = [j.extract().strip().replace("\r\n", "").replace("                            ", "").replace("                           ", "") for j in [i.css("h3::text") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_questions = "|".join(faq_questions)
            faq_answers = [j.css("p::text").extract_first().strip().replace("\r\n","").replace("                                 ","") for j in [i.css("div.card") for i in response.css("div.col-lg-10.col-sm-12")][0]]
            faq_answers = "|".join(faq_answers)
        except:
            faq_questions = None
            faq_answers = None

        module = []
        for i in response.css("div.accordion.md-accordion").css("h5.mb-0::text"):
            if i is not None:
                module.append(i.extract())
        for j in response.css("div.accordion.md-accordion").css("h4.mb-0::text"):
            if j is not None:
                module.append(j.extract().strip())
        modules = []
        for ele in module:
            if ele.strip():
                modules.append(ele)
        modules = modules[:-3]
        #modules = [j.extract() for j in response.css("div.accordion.md-accordion").css("h5.mb-0::text")]

        sub_mod = [i.css("li::text").extract() for i in response.css("div.col-lg-12")][:-10]
        sub_mod = sub_mod[3:]
        modlist = list()
        # print(len(sub_mod))
        modulenum = 1
        for i in range(len(modules)):
            module = f"<p><strong>Module {modulenum}: {modules[i]}</strong>"
            modlist.append(module)
            # print(module)
            try:
                submodnum = 1
                for j in sub_mod[i]:
                    submodule = f"<br>{submodnum}. {j}"
                    modlist.append(submodule)
                    submodnum += 1
            except:
                pass

            modulenum += 1
            modlist.append('</p>')

        contents = "".join(modlist)
        #print(contents)

        items["title"] = title
        items["desc"] = desc
        items["contents"] = contents
        items["cover_video"] = cover_video
        items["cover_img"] = cover_img
        items["content_module"] = content_module
        items["total_duration"] = total_duration
        items["course_start_date"] = course_start_date
        items["course_duration"] = course_duration
        items["display_price"] = display_price
        items["instructor"] = instructor
        items["inst_desig"] = inst_desig
        items["inst_img"] = inst_img
        items["inst_bio"] = inst_bio
        items["avg_sal_hike"] = avg_sal_hike
        items["high_sal"] = high_sal
        items["reviewer_names"] = reviewer_names
        items["reviewer_photos"] = reviewer_photos
        items["reviews"] = reviews
        items["faq_questions"] = faq_questions
        items["faq_answers"] = faq_answers

        yield items