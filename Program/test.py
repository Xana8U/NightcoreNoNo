from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re

capab = DesiredCapabilities.FIREFOX
capab["marionette"] = False

#   Runs default firefox driver as marionette is disabled (marionette=
driver = webdriver.Firefox(capabilities=capab)

driver.get("http://plug.dj/nightblue")
time.sleep(25)

song = driver.find_element_by_id("now-playing-bar")
song_attribute = song.get_attribute("innerHTML")

if re.search("Basta", song_attribute):
    print("yes")
    driver.execute_script("var a = document.getElementsByClassName('button')[0].click();")
else:
    print("no")
