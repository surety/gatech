from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = None

def setup_module():
    global driver
    driver = webdriver.Safari()
    print('Tool ready!')

def teardown_module():
    driver.quit()
    print('Tool terminated!')

#needs to be organized properly
def search_classes(subject, term = 'Fall 2020', time = None, days = None, instructor = None):
    driver.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
    wait = WebDriverWait(driver, 10)
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
            template.append(raw_data[i])
        data.append(template)

    return data
