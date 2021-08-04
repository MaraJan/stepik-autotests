from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pytest
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    
links_massive = ['https://stepik.org/lesson/236895/step/1',
                 'https://stepik.org/lesson/236896/step/1',
                 'https://stepik.org/lesson/236897/step/1',
                 'https://stepik.org/lesson/236898/step/1',
                 'https://stepik.org/lesson/236899/step/1',
                 'https://stepik.org/lesson/236903/step/1',
                 'https://stepik.org/lesson/236904/step/1',
                 'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('links', links_massive)
def test_open_browser(browser, links):
    
    browser.implicitly_wait(10)
        
    link1 = f'{links}'
    browser.get(link1)
    
    option1 = browser.find_element_by_css_selector("textarea.ember-text-area.ember-view.textarea.string-quiz__textarea")
    option1.send_keys(str(math.log(int(time.time()))))
   
    button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
                )
    button.click()
    
    message_text = WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
                ).text
        
    assert message_text == "Correct!", \
    f"Wrong text {message_text}"
        