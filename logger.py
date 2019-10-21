from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
options.add_argument(f'user-agent={userAgent}')

webdriver_path = r'chromedriver.exe'
browser = webdriver.Chrome(options = options, executable_path = webdriver_path)

xpaths = {
    'username' : '//*[@id="user"]',
    'password' : '//*[@id="password"]',
    'login button' : '//*[@id="regform"]/input[2]',
    'logout button' : '/html/body/p/a'
}

def login():
    url = 'http://192.168.231.6/cgi-bin/login'
    browser.get(url)
    try:
        element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "user")))
    except NoSuchElementException:
        print("element cant be found")
    # browser.find_element_by_xpath(xpaths['username']).send_keys("TEDD024K")
    # browser.find_element_by_xpath(xpaths['password']).send_keys("TEDD024K")
    # browser.find_element_by_xpath(xpaths['login button']).click()
    browser.find_element_by_id('user').send_keys("TEDD024K")
    browser.find_element_by_id('password').send_keys("TEDD024K")
    browser.find_element_by_class_name('button').click()
    browser.quit()

def logout():
    url2 = 'http://192.168.231.6/cgi-bin/login?cmd=popup'
    browser.get(url2)
    browser.find_element_by_xpath(xpaths['logout button']).click()

login()


