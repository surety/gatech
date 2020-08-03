import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print('Connecting...')
driver = webdriver.Safari()
driver.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
wait = WebDriverWait(driver, 10)
print('Done.')

print('Selecting term...')
search_by_term = driver.find_element_by_name('p_term')
submit = driver.find_element_by_xpath("//input[@type='submit']")
Select(search_by_term).select_by_value('202008')
submit.submit()
#time.sleep(3)
print('Done.')

print('Selecting subject...')
subject_select = wait.until( EC.presence_of_element_located( (By.ID, "subj_id")) )
url = driver.current_url
submit = wait.until( EC.presence_of_element_located( (By.XPATH, "//input[@type='submit']") ))
Select(subject_select).select_by_visible_text('Accounting')
submit.submit()
wait.until(EC.url_changes(url))
print('Done.')

print('Fetching classes...')
#(0-6), (7-13)
data_labels = ['Type','Time','Days','Where','Date Range','Schedule Type','Instructors']
classes_elements = driver.find_elements_by_xpath("//td[@class='dddefault']")
classes_data = []
for element in classes_elements:
	if not len(element.text) > 50:
		classes_data.append(element.text)
class_titles = []
classes = []
classes_available = int(len(classes_data) / 7)
for i in range(classes_available):
	temp = []
	for i in range(7*i, 7*i + 7):
		temp.append(classes_data[i])
	classes.append(temp)
print(classes_available)
for c in classes:
	print(c)
print('Done.')

print("Tool teardown...")
driver.quit()
print("Terminated!")
