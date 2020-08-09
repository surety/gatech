import json

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = None
wait = None
settings = None

def setup_module():
    global driver
    global wait
    global settings
    driver = webdriver.Safari()
    wait = WebDriverWait(driver, 10)
    print('Tool ready!')

def teardown_module():
    driver.quit()
    print('Tool terminated!')

#needs to be organized properly
#change term from string to term id
def search_classes(subject, term = 'Fall 2020', time = None, days = None, instructor = None):
    driver.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
    search_by_term = driver.find_element_by_name('p_term')
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    Select(search_by_term).select_by_visible_text(term)
    submit.submit()

    subject_select = wait.until(EC.presence_of_element_located((By.ID, "subj_id")))
    url = driver.current_url
    submit = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    Select(subject_select).select_by_visible_text(subject)
    submit.submit()
    wait.until(EC.url_changes(url))
    elements = driver.find_elements_by_xpath("//td[@class='dddefault']")
    raw_data = []
    for element in elements:
        if not len(element.text) > 50:
            raw_data.append(element.text)
    num_classes = int(len(raw_data) / 7)
    data =[]
    for i in range(num_classes):
        template = []
        for j in range(7*i, 7*i + 7):
            template.append(raw_data[j])
        data.append(template)

    return data

#def get_prefrences(): pass

def get_desired_classes():
    classes = []
    data = json.load(open('settings.json'))
    for crn in data['desiredClasses']:
        classes.append(crn)

    return classes

def is_available(crn, term = 202008):
    driver.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=%s&crn_in=%s' % (term, crn))
    sr_xpath = "//table[@summary='This layout table is used to present the seating numbers.']//tr[2]/td[3]"
    seats_remaining = wait.until(EC.presence_of_element_located((By.XPATH, sr_xpath)))

    return not int(seats_remaining.text) == 0

#def remove_prefrence(crn): pass
def remove_desired_class(crn): pass
#def add_prefrence(crn): pass
#def add_desired_class(crn): pass

def register(crn): pass

#def unregister(): pass

#make a seprate file for the following functions
def idle_registration():
    while not get_desired_classes() == None:
       for crn in get_desired_classes():
            if is_available(crn):
                register(c) #will catch errors and confirm registration
                remove_desired_class(c)

    pass
