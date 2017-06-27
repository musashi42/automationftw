import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import gmtime, strftime
import sys

from xvfbwrapper import Xvfb

display = Xvfb()
display.start()

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
binary = FirefoxBinary(r'/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

links_file = open(sys.argv[1], 'r')

links = links_file.readlines()


for link in links:
    link = link.rstrip('\n')
    driver.get(link)
    times = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    driver.save_screenshot(times + '.png')
    print "Screenshot " + url + " saved"
driver.quit()
display.stop()
