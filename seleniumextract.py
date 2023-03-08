from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
def getdata_by_xpath(url,xpath,option):
    driver.get(url)
    # assert "Google" in driver.title
    elem = driver.find_element("xpath", xpath)
    if option=='value':
        return elem.get_attribute('value')
    elif option=='href':
        return elem.get_attribute('href')
    elif option=='innerhtml':
        return elem.text.split('\n')
    else:
        return []
def getdata_by_event_xpath(url,xpath,listrange,option,actionxpath,actioncount,):
    listrange+=1
    driver.get(url)
    driver.maximize_window()
    result=[]
    # assert "Google" in driver.title
    for i in range(actioncount):
        button = driver.find_element("xpath",actionxpath)
        for index in range(1,listrange):
            elem=driver.find_element("xpath", xpath.format(index))
            if option == 'value':
                result.append(elem.get_attribute('value'))
            elif option == 'href':
                result.append(elem.get_attribute('href'))
            elif option == 'innerhtml':
                result.append(elem.text.split('\n'))
            else:
                result.append([])
        print(i)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", button)
    return result

def close_drive():
    driver.close()