from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common import action_chains, keys
import time
import getpass
import re

# LOGIN INFORMATION
# LOGIN_VAR
print("Plug.DJ Email Login")
username = input("Email: ")
password = getpass.getpass('Password: ')

#   Disabling marionette is required for this to work
capab = DesiredCapabilities.FIREFOX
capab["marionette"] = False

#   Runs default firefox driver as marionette is disabled (marionette=
driver = webdriver.Firefox(capabilities=capab)

#   Actions, key combinations
action = action_chains.ActionChains(driver)

#   Open Plug.dj in small window
driver.set_window_size(600, 300)
driver.get("https://plug.dj/")



#   Opens users browser and takes him to login screen
#   START----------- ALTERNATIVE (UGLY) -----------v
# action.send_keys(keys.Keys.LEFT_CONTROL + keys.Keys.LEFT_SHIFT + 'k')
# action.perform()
# action.send_keys(keys.Keys.ENTER)
# time.sleep(2)
# action.send_keys("""document.querySelectorAll("button")[2].click();""" + keys.Keys.ENTER)
# action.perform()
# time.sleep(1)
# action.send_keys("""document.querySelectorAll("button")[40].click();""" + keys.Keys.ENTER)
# action.perform()
#   END----------- ALTERNATIVE(UGLY) ------------^
driver.execute_script("""document.querySelectorAll("button")[2].click();""")
time.sleep(2)
driver.execute_script("""document.querySelectorAll('button')[8].click();""")
time.sleep(1)

#   Plug.DJ Login
driver.find_element_by_class_name('log-email-container').click()
action.send_keys(username + keys.Keys.TAB + password + keys.Keys.ENTER)
action.perform()
time.sleep(2)

#   joinNB3
driver.get("https://plug.dj/nightblue")
driver.maximize_window()
#plugging in
time.sleep(10)

# check if song is nightcore and mutes it by pressing button0(volume mute)
while True:
    song = driver.find_element_by_id("now-playing-bar")
    song_attribute = song.get_attribute("innerHTML")
    volume = driver.find_element_by_css_selector("#volume span")
    volume_attribute = volume.get_attribute("innerHTML")
    if volume_attribute == "0%" and re.search("ightcore", song_attribute) == 0:
        driver.execute_script("var a = document.getElementsByClassName('button')[0].click();")
    elif re.search("ightcore", song_attribute) == 1:
        driver.execute_script("var a = document.getElementsByClassName('button')[0].click();")
    time.sleep(2)
