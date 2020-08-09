# 8/8/20 - By: surety
# Purpose: Test registration function

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

# Use ' ' to assaign values to variables.
# For example: if my password is yomama123 then change None to 'yomama123'

username = ''
password = ''

# Assaign desired class crn to 'new_crn'
new_crn = None

# Be fucking careful with this one.
# Imagine that whatever you type for 'old_crn' is FINAL
old_crn = None

# This will just boot up an automated browser.
# Don't mess with it, it'll stop the processes.
print('Welcome...')
driver = webdriver.Safari()
wait = WebDriverWait(driver, 10)
print('Tool ready!')


print('Login in...')
url = 'https://login.gatech.edu/cas/login'
driver.get(url)
user_element = wait.until(EC.presence_of_element_located( (By.ID, "username") ))
pass_element = wait.until(EC.presence_of_element_located( (By.ID, "password") ))
login_element = wait.until(EC.presence_of_element_located( (By.XPATH, "//input[@type='submit']") ))

user_element.send_keys(username)
pass_element.send_keys(password)
login_element.click()
time.sleep(1)
wait.until(EC.url_changes(url))
print('Done.')


print('***CHANGING CLASSES...***')
driver.get('https://oscar.gatech.edu')
#time.sleep(5)
#url = 'https://oscar.gatech.edu/pls/bprod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu'
#driver.get(url)

sal = wait.until(EC.presence_of_element_located( (By.XPATH, "//a[@class='btn btn-link btn-block']") ))
sal.click()
services = wait.until(EC.presence_of_element_located( (By.XPATH, "//img[@title='Student Services and Financial Aid']") ))
services.click()
registration = wait.until(EC.presence_of_element_located( (By.LINK_TEXT, "Registration") ))
registration.click()
add_or_drop_link = wait.until(EC.presence_of_element_located( (By.LINK_TEXT, "Add or Drop Classes") ))
add_or_drop_link.click()
submit_term = wait.until(EC.presence_of_element_located( (By.XPATH, "//input[@value='Submit']") ))
submit_term.click()

#unregister old class
print('WARNING!!! Unregistering class...')
table_data = wait.until(EC.presence_of_elements_located( (By.XPATH, "//table[@summary='Current Schedule']//td") ))

for i in range(0, len(table_data)):
    if (i % 10) == 0 and table_data[i - 7] == crn_old:
        action = wait.until(EC.presence_of_elements_located( (By.XPATH, "//select[@id='action_id%d']" % int(i / 10)) ))

Select( action ).select_by_visible_text('**Delete (Web)')
submit_changes = wait.until(EC.presence_of_element_located( (By.XPATH, "//input[@value='Submit Changes']") ))
submit_changes.submit()
print('Done!')

#register for new class
print('Registering class...')
new_crn_element = wait.until(EC.presence_of_element_located( (By.ID, "crn_id1") ))
submit_changes = wait.until(EC.presence_of_element_located( (By.XPATH, "//input[@value='Submit Changes']") ))
new_crn_element.send_keys(new_crn)
submit_changes.submit()
print('Done!')

print('Changes complete!!!')


print('Goodbye...')
driver.quit()
print('Tool terminated!')
