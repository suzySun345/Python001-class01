from fake_useragent import UserAgent
import requests
ua = UserAgent(verify_ssl=False)
header = {
'origin': 'https://shimo.im',
'x-requested-with': 'XmlHttpRequest',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'dnt': '1',
'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
'referer': 'https://shimo.im/login?from=home',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
}
url = "https://shimo.im/lizard-api/auth/password/login"
url2 = "https://shimo.im/dashboard/used"
form_data = {
    'email': 'sunsunsisiyu@126.com',
    'password': 'ssy350009513'
}
with requests.Session() as s:
    resp = s.post(url, data=form_data, headers=header)
    print(resp.status_code)
    print(resp.cookies)

    res = s.get(url2, headers=header)
    print(res.status_code)
    print(res.text)
    
d = requests.Session()
resp2 = d.get(url2)
print(resp2.text)