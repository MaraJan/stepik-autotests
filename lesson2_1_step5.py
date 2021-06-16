from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    
    option1 = browser.find_element_by_css_selector("input#answer.form-control")
    option1.send_keys(y)
    
    option2 = browser.find_element_by_css_selector("label.form-check-label")
    option2.click()
    
    option3 = browser.find_element_by_css_selector("[for='robotsRule']")
    option3.click()
    
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()