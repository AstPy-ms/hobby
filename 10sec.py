import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
browser = Firefox(executable_path='/usr/share/bin/geckodriver', options=options)

browser.get('https://totoraj930.github.io/10sec/')
time.sleep(0.5)
browser.find_element_by_id("button").click()
time.sleep(9.77)
browser.find_element_by_id("button").click()