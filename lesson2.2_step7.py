from selenium import webdriver
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"  
    browser = webdriver.Chrome()
    browser.get(link)
    
    option1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    option1.send_keys("Iurii")
    
    option2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    option2.send_keys("Vladimirovich")
    
    option3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    option3.send_keys("Sobaka@bk.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'piy.txt')
    option4 = browser.find_element_by_css_selector("input#file")
    option4.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()