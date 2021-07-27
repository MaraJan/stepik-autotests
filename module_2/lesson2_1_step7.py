from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure1 = browser.find_element_by_id("treasure")
    treasure_values = treasure1.get_attribute("valuex")
    
    x = treasure_values
    y = calc(x)
    
    option1 = browser.find_element_by_css_selector("input#answer")
    option1.send_keys(y)
    
    option2 = browser.find_element_by_css_selector("input#robotCheckbox")
    option2.click()
    
    option3 = browser.find_element_by_css_selector("input#robotsRule.check-input")
    option3.click()
    
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()