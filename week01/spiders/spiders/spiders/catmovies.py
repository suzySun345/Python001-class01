import scrapy
from scrapy import Selector
from spiders.items import SpidersItem

class CatmoviesSpider(scrapy.Spider):
    name = 'catmovies'
    allowed_domains = ['maoyan.com']
    #start_urls = ['https://movie.douban.com/top250']
    start_urls = ['https://maoyan.com/films?showType=3']
    # custom_settings = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    #     'Cookie': '__mta=208024493.1593227034107.1593229103641.1593229376607.16; uuid_n_v=v1; uuid=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; _csrf=10d20465fa55d18cfc0a93b160f1cd503add5b70481e90e424a24ac3101511ed; _lxsdk_cuid=172f3bb3d2cc8-088f8748df3d1b-4353760-e1000-172f3bb3d2cc8; _lxsdk=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; mojo-uuid=6e0c8bf6ecc118a0c54db0e0641a8976; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593227034,1593227043,1593228659; mojo-session-id={"id":"db9feb6d07b8a02363d3e3b39186c199","time":1593246167502}; mojo-trace-id=8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593247030; __mta=208024493.1593227034107.1593229376607.1593247030225.17; _lxsdk_s=172f4df3168-44-d13-7b3%7C%7C12',
    #     'Connection': 'keep-alive',
    #     }
    # def parse(self, response):
    #     pass

    def start_requests(self):

        url = 'https://maoyan.com/films?showType=3'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        cookies = '__mta=208024493.1593227034107.1593229103641.1593229376607.16; uuid_n_v=v1; uuid=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; _csrf=10d20465fa55d18cfc0a93b160f1cd503add5b70481e90e424a24ac3101511ed; _lxsdk_cuid=172f3bb3d2cc8-088f8748df3d1b-4353760-e1000-172f3bb3d2cc8; _lxsdk=D503DB20B82211EA8B56A5EC695B0A73A76BDE81FEDA4546ABAA69BD366C3CBF; mojo-uuid=6e0c8bf6ecc118a0c54db0e0641a8976; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593227034,1593227043,1593228659; mojo-session-id={"id":"db9feb6d07b8a02363d3e3b39186c199","time":1593246167502}; mojo-trace-id=8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593247030; __mta=208024493.1593227034107.1593229376607.1593247030225.17; _lxsdk_s=172f4df3168-44-d13-7b3%7C%7C12'
        header = {'user-agent': user_agent, 'Cookie': cookies, 'Connection': 'keep-alive'}
        
        
        # for i in range(10):
        #     url = f'https://maoyan.com/films?showType=3&offset={i*30}'

        yield scrapy.Request(url=url, headers=header, callback=self.parse)
    
    def parse(self, response):
        print(response.url)
        
        
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

            item = SpidersItem()
            item['name'] = res_name
            item['m_type'] = res_type
            item['m_time'] = res_time
            
            yield item


                