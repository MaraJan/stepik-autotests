from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    people_radio = browser.find_element_by_id("peopleRule")
    
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()