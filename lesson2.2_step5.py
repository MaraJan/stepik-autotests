from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    link = "http://SunInJuly.github.io/execute_script.html"  
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    y = calc(x)
    
    option1 = browser.find_element_by_css_selector("input#answer.form-control")
    option1.send_keys(y)
    
    option2 = browser.find_element_by_css_selector("input#robotCheckbox.form-check-input")
    option2.click()
    
    
    
    option3 = browser.find_element_by_css_selector("input#robotsRule.form-check-input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
    option3.click()
    
    
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    
    time.sleep(10)
    browser.quit()
