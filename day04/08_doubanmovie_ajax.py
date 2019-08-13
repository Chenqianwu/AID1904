import requests

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?' \
                   'type=11&interval_id=100%3A90&action=&' \
                   'start=0&limit={}'
        # 正则批量处理headers
        # 1. Pycharm中,Ctrl+r,选中　Regex
        # (.*): (.*)
        # '$1': '$2',
        # 点击Replace All
        self.headers = {
            'Accept': '*/*',
            # 慎用: 是否支持压缩,浏览器会自动解压缩,程序不会
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'll="108288"; bid=aSBSguls21o; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1563869922%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DLhtlEVPyxYNpp0kQ0G_fAgW99F63tVN1zdWjjykcgmRItkxMvsmebYYNiiG8xSfz%26wd%3D%26eqid%3Df4a20ed0000c68d1000000035d36c2dc%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.294047153.1563869922.1563869922.1563869922.1; __utmb=30149280.0.10.1563869922; __utmc=30149280; __utmz=30149280.1563869922.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1049979206.1563869922.1563869922.1563869922.1; __utmb=223695111.0.10.1563869922; __utmc=223695111; __utmz=223695111.1563869922.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=2yqEFWFrvkTDxxdzao2zxhhN2aA00YLX; _vwo_uuid_v2=DFCF0832EDBDC20E4B00BA861174082E8|6dde682338779ea97188011aa0abe344; _pk_id.100001.4cf6=cc5a01a84b5030df.1563869922.1.1563873081.1563869922.',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
    # 请求+解析
    def get_film_info(self,url):
        # res.json() -> 返回python数据类型(列表或者字典)
        # html_json: [{电影1},{电影2},...]
        html_json = requests.get(
            url = url,
            headers = self.headers
        ).json()
        # for遍历每个电影
        for film in html_json:
            # 名称
            name = film['title']
            # 评分
            score = film['score']

            print(name,score)

    def main(self):
        limit = input('请输入电影数量:')
        url = self.url.format(limit)
        self.get_film_info(url)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()

























