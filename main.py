import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def scroll():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1,total_height,3):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    for i in range(total_height,1,-3):
        driver.execute_script("window.scrollTo(0, {});".format(i))


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.


#Test Home page

driver.get('https://www.thesparksfoundationsingapore.org/');
time.sleep(5)
print("Title :",driver.title)
time.sleep(1)
if driver.find_element_by_xpath("//img[@src='/images/logo_small.png']") != None:
    print("Logo exists")
else:
    print("Logo does not exists!!")
time.sleep(1)
Dnav=driver.find_element_by_tag_name("nav").is_displayed()
print("Navigation bar appears :",Dnav)
time.sleep(2.5)


# Maximizing window

driver.maximize_window()
time.sleep(4)



#Test About Us page

driver.find_element_by_link_text("About Us").click()
time.sleep(1)

m=driver.find_element_by_link_text("Vision, Mission and Values")
ActionChains(driver).move_to_element(m).perform()
time.sleep(2)

driver.find_element_by_link_text("Vision, Mission and Values").click()
time.sleep(2)

scroll()
time.sleep(0.5)


######################################################

#Test Another components
m=driver.find_element_by_link_text("Guiding Principles")
ActionChains(driver).move_to_element(m).perform()
time.sleep(1)

driver.find_element_by_link_text("Guiding Principles").click()
time.sleep(2)


scroll()
time.sleep(2)
#####################################################

driver.find_element_by_link_text("Policies and Code").click()
time.sleep(0.5)

#####################################################

m=driver.find_element_by_link_text("Policies")
ActionChains(driver).move_to_element(m).perform()
time.sleep(1)

driver.find_element_by_link_text("Policies").click()
time.sleep(2)


scroll()
time.sleep(2)

###################################################

driver.find_element_by_link_text("Programs").click()
time.sleep(1)
driver.find_element_by_link_text("LINKS").click()
time.sleep(1)
driver.find_element_by_link_text("Join Us").click()
time.sleep(1)
driver.find_element_by_link_text("Contact Us").click()
time.sleep(1)

###########################################

driver.find_element_by_link_text("Join Us").click()
time.sleep(1)


m=driver.find_element_by_link_text("Why Join Us")
ActionChains(driver).move_to_element(m).perform()
time.sleep(1)

driver.find_element_by_link_text("Why Join Us").click()
time.sleep(2)

for i in range(1, 650, 3):
    driver.execute_script("window.scrollTo(0, {});".format(i))


#Testing Key functions

time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Full Name']").send_keys("Subhram Patel")
time.sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Email or Phone Number']").send_keys("subhram336@gmail.com")
time.sleep(3)
S1 = Select(driver.find_element_by_class_name("form-control"))
S1.select_by_visible_text("Intern")

###########################################

time.sleep(4)

#Close the Page
driver.quit()






