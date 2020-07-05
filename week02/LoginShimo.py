from selenium import webdriver
from fake_useragent import UserAgent
import requests
import time
def useSelenium():
    global driver
    driver = webdriver.Chrome()
    res = driver.get("https://shimo.im/desktop")

    driver.find_element_by_name('mobileOrEmail').send_keys('sunsunsisiyu@126.com')
    driver.find_element_by_name('password').send_keys('ssy350009513')
    driver.find_element_by_tag_name('button').click()
    time.sleep(3)
    #driver.close()
    #print(driver.get_cookies)
def useRequest():
    ua = UserAgent(verify_ssl=False)
    header = {
    'authority': 'shimo.im',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'origin': 'https://shimo.im',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'accept': '*/*',
    'sec-fetch-dest': 'empty',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://shimo.im/login?from=home',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    url = "https://shimo.im/lizard-api/auth/password/login"
    form_data = {
        'email': 'sunsunsisiyu@126.com',
        'password': 'ssy350009513'
    }
    s = requests.Session()
    r1 = s.post(url, data=form_data, headers=header)
    print(r1.text)
    url2 = "https://shimo.im/dashboard/used"
    r = s.get(url, headers=header)
    print(r.text)
    #newsession = requests.Session()
    #newsession.get(url2,cookies=s.cookies)
    
    

if __name__=='__main__':
    #useSelenium()
    useRequest()