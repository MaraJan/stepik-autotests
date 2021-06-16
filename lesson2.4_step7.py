from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    option = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id('book')
    button.click()
    
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    y = calc(x)
    
    option1 = browser.find_element_by_css_selector('input#answer.form-control')
    option1.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 100);")
    button1 = browser.find_element_by_css_selector('button#solve.btn.btn-primary')  
    button1.click()
    
    
finally:
    time.sleep(20)
    browser.quit()