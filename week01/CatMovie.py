#encoding = utf-8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# preparation before request
myurl = "https://maoyan.com/films?showType=3"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookies = '__mta=208024493.1593227034107.1593229103641.1593229376607.16; uuid_n_v=v1; uuid=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; _csrf=10d20465fa55d18cfc0a93b160f1cd503add5b70481e90e424a24ac3101511ed; _lxsdk_cuid=172f3bb3d2cc8-088f8748df3d1b-4353760-e1000-172f3bb3d2cc8; _lxsdk=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; mojo-uuid=6e0c8bf6ecc118a0c54db0e0641a8976; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593227034,1593227043,1593228659; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593254194; __mta=208024493.1593227034107.1593229376607.1593254194244.17; _lxsdk_s=172f6288371-282-fd1-6dd%7C%7C1'
header = {'user-agent': user_agent, 'Cookie': cookies, 'Connection': 'keep-alive'}

# make a get request to myurl to get html text
resp = requests.get(myurl, headers=header)
print(resp.text)

# use bearutiful soup to parser html text
parser_res = bs(resp.text, 'html.parser')
movie_list = parser_res.find_all("div", attrs={'class': 'movie-hover-info'}, limit=10 )
movie_set = []
for each in movie_list:
    #dtag = each.find("div", attrs={'class': 'movie-hover-info'})
    dtags = each.find_all("div",attrs={'class':'movie-hover-title'})
    movie_name = dtags[0].find("span").text
    movie_type = dtags[1].get_text(strip=True).split(':')[1]
    movie_time = dtags[3].get_text(strip=True).split(':')[1]
    print(movie_name)
    print(movie_type)
    print(movie_time)
# create a file to save the movies info

    movie_record = {'电影': movie_name, '类型': movie_type, '上映时间': movie_time}
    movie_set.append(movie_record)

movie_df = pd.DataFrame(data=movie_set)
movie_df.to_csv("./result.csv",encoding="utf-8", index=False, mode="w")


