import scrapy
from fake_useragent import UserAgent
from scrapy import Selector
from IPproxy.items import IpproxyItem
class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['https://maoyan.com/films?showType=3']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        ua = UserAgent(verify_ssl=False)
        cookies = '__mta=208024493.1593227034107.1593229103641.1593229376607.16; uuid_n_v=v1; uuid=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; _lxsdk_cuid=172f3bb3d2cc8-088f8748df3d1b-4353760-e1000-172f3bb3d2cc8; _lxsdk=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; mojo-uuid=6e0c8bf6ecc118a0c54db0e0641a8976; _csrf=d205ccf89d26b6dea9e3b6972230b6808021092ef098a6aed90ad8cd95815504; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593227034,1593227043,1593228659,1593923380; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; mojo-session-id={"id":"f99ba9c6bd3e32cab2044a6aef7e5390","time":1593959310357}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593959310; __mta=208024493.1593227034107.1593229376607.1593959310418.17; _lxsdk_s=1731f60e42e-336-dd2-00%7C%7C2'
        header = {
            'user-agent': str(ua.chrome),
            'host': 'maoyan.com',
            'Connection': 'keep-alive',
            'Cookie': cookies
        }
        yield scrapy.Request(url,headers=header,callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath("//div[@class='movie-hover-info']")
        for i in range(10):
            movie = movies[i].xpath("./div[contains(@class,'movie-hover-title')]")
            movie_name = movie[0].xpath("./span[1]/text()")
            movie_type = movie[1].xpath("./text()")
            movie_time = movie[3].xpath("./text()")

            res_name = movie_name.get()
            res_type = movie_type.extract()[1].strip()
            res_time = movie_time.extract()[1].strip()
            print(res_name)
            print(res_type)
            print(res_time)

            item = IpproxyItem()
            item['name'] = res_name
            item['m_type'] = res_type
            item['m_time'] = res_time
            
            yield item
