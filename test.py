import time
from selenium import webdriver

driver = webdriver.Chrome('/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');