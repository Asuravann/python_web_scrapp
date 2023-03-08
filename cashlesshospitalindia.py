from extractdata import get_school_urls,extract_schools,end_program
from makecsv import make_csv
from seleniumextract import close_drive,getdata_by_xpath,getdata_by_event_xpath
option=['href','innerhtml','value']
# def gethospitallist(url,xpath,opt,listrange):
#     hospital=[]
#     for i in range(1,listrange):
#         hospital.append(getdata_by_xpath(url,xpath.format(i),opt)
#     return hospital

url="http://www.cashlesshospitalindia.com/hospital.html"
xpath="/html/body/div[2]/div[2]/div[1]/div/div/div/albr/table/tbody/tr/td[1]/div[1]/table/tbody/tr[{}]/td"

result=getdata_by_event_xpath(url,xpath,10,option[1],"/html/body/div[2]/div[2]/div[1]/div/div/div/albr/table/tbody/tr/td[1]/div[1]/div[4]/a[2]",1000)
make_csv('cash-less-hospital-india.csv',["column"+str(i) for i in range(len(result[0]))],result)

end_program()

#/html/body/div/div[2]/div/table[1]/tbody/tr/td[2]


