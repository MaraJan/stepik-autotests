from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    y = calc(x)
    
    option1 = browser.find_element_by_css_selector("input#answer.form-control")
    option1.send_keys(y)
    
    button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
    button1.click()
    
finally:
    
    time.sleep(10)
    browser.quit()