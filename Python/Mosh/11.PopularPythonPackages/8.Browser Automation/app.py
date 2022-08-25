from selenium import webdriver
browser = webdriver.Chrome()

browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("name")
password_box = browser.find_element_by_id("login_field")
password_box.send_keys("pass")
password_box.submit()

assert "dipu" in browser.page_source

profile_link = browser.find_element_by_class_name("user-name")
link_lable = profile_link.get_attribute('innerHTML')

assert "dipu" in link_lable

# browser.quit()
