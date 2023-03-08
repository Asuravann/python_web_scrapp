from extractdata import get_school_urls,extract_schools,end_program
from makecsv import make_csv
option=['href','innerhtml','value']
school_urls=get_school_urls('https://www.internationalschoolsearch.com/international-schools-in-india',342,
                    "/html/body/div/div[2]/div[3]/div/div[{}]/div/h3[2]/a",option[0])
result=extract_schools(school_urls,"/html/body/div/div[2]/div/table[1]/tbody/tr/td[2]","/html/body/div/div[2]/div/table[1]/tbody/tr/td[1]",
    option[1])
print(result)
make_csv('__international-schools-in-india.csv',["column"+str(i) for i in range(len(result[0]))],result)

end_program()

#/html/body/div/div[2]/div/table[1]/tbody/tr/td[2]


