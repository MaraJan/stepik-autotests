from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(a,b):
    return str(int(a)+int(b))

try:
    
    link = "http://suninjuly.github.io/selects1.html"  
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = browser.find_element_by_css_selector("span#num1.nowrap").text
    b = browser.find_element_by_css_selector("span#num2.nowrap").text
    c = calc(a,b)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)
    
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()