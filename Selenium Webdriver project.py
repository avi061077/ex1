# 1. Write a script which will open the following
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.ie.options import Options

import time

# chrome_driver = webdriver.Chrome('C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')

# chrome_driver.get('http://www.walla.co.il')
# firefox_driver = webdriver.Firefox()
# firefox_driver.get('http://www.ynet.co.il')


# # 2. In one of the browsers you have open, do the following
# web_title = "Walla! - אתר התכנים המוביל בישראל"
# actual_title = chrome_driver.title
# assert actual_title == web_title, f"Expected title '{web_title}', but got '{actual_title}'"
# chrome_driver.refresh()
# actual_title = chrome_driver.title
# assert actual_title == web_title, f"Expected title '{web_title}', but got '{actual_title}' after refreshing"

# 3. Open a few browsers, locate any element, does the element has the same locator in
# the other browser?
# answer = yes


# 4. Create a test with the following

# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# chrome_driver.get('https://translate.google.com/')
# chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys('יאללה בלאגן')


# 5. Open Youtube web page


# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# chrome_driver.get('https://www.youtube.com/')
# chrome_driver.find_element(By.NAME, "search_query").send_keys("עדן חסון ")
# chrome_driver.find_element(By.ID, "search-icon-legacy").click()

# 6. Open Chrome browser on Google Translate website: https://translate.google.com/

# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# chrome_driver.get('https://translate.google.com/')
# chrome_driver.find_element(By.XPATH,
#                            '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
# print(f"Translation field by XPath: {chrome_driver}")
#
# chrome_driver.find_element(By.ID, "source")
# print(f"Translation field by ID: {chrome_driver}")
#
# chrome_driver.find_element(By.NAME, "text")
# print(f"Translation field by name: {chrome_driver}")


# 7. Open Chrome browser on Facebook website https://www.facebook.com/

# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# chrome_driver.get('https://www.facebook.com/')
# chrome_driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('avi0610@gmail.com')
# chrome_driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('xxxxxx')
# chrome_driver.find_element(By.ID, "u_0_5_9t").click()
#
# input()
# Challenges:
# 8
# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# web = chrome_driver
# web.get('http://www.walla.co.il')
# web.delete_all_cookies()
# print(web.get_cookies())


# # 9
#
#
# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# web = chrome_driver
# web.get('https://github.com/')
# web.find_element(By.NAME, 'q').send_keys("Selenium")
# web.find_element(By.NAME, 'q').send_keys(Keys.RETURN)


# 10
# chrome

# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
#
# executable_driver = webdriver.Chrome(executable_path='C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe', options=chrome_options)
# executable_driver.get("https://www.n12.co.il")

# # firefox
# firefox_driver = webdriver.Firefox()
# firefox_options = Options()
# firefox_options.set_preference("extensions.enabledScopes", 0)
# firefox_executable_driver = webdriver.Firefox(options=firefox_options)
# firefox_driver.get('http://www.ynet.co.il')


# internet Explorer.

# ie_driver = "C:/firefox/IEDriverServer.exe"
# ie_options = Options()
# ie_options.ignore_protected_mode_settings = True
# ie_driver_web = webdriver.Ie(executable_path="C:/firefox/IEDriverServer.exe", options=ie_options)
# ie_driver_web.get('http://www.ynet.co.il')
# input()

# 11
# chrome
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_driver = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe')
#
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# driver_chrome = webdriver.Chrome(
#     'C:/Users//User\OneDrive - Net-Core\Documents\DEVOPS\chromedriver_win32\chromedriver.exe', options=chrome_options)
#
# driver_chrome.get("https://www.cnn.com")
