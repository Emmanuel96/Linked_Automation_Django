import time
from selenium import webdriver

driver = webdriver.Chrome()
# Optional argument, if not specified will search the PATH.
driver.get('http://www.google.com/')
