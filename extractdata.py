from seleniumextract import close_drive,getdata_by_xpath


def get_school_urls(url,listrange,xpath,option):
    schoolurls = []
    for i in range(1, listrange):
        print(i)
        schoolurls.append(getdata_by_xpath(url,xpath.format(i), option))
    return schoolurls

def extract_schools(urls,xpath,alternatexpath,option):
    schools=[]
    for index,url in enumerate(urls):
        data=getdata_by_xpath(url, xpath, option)
        if len(data)==1:
            data = getdata_by_xpath(url, alternatexpath, option)
        schools.append(data)
        print(url)

    return schools


def end_program():
    close_drive()

