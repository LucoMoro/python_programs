from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element("Sign in")
signin_link.click()

username_box = browser.find_element("login_field")
username_box.send_keys("name_profile")
password_box = browser.find_element("password")
password_box.send_keys("password_profile")
password_box.submit()

assert "name_profile" in browser.page_source 
#if the name_profile isn't in the webpage there will 
# be an error

profile_link = browser.find_element("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "name_profile" in link_label