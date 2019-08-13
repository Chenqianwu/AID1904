import requests
import re
import execjs

class BaiduTranslateSpider(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "BAIDUID=2619E4B40580C3B077FF47135A00E390:FG=1; PSTM=1561529240; BIDUPSID=6E51187F13540BD223A2CC75D5DAD043; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; PSINO=1; td_cookie=18446744071276835184; H_PS_PSSID=1456_21115_29578_29518_28519_29098_29568_28837_29220_29588; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563954537,1564019919,1564022523,1564024494; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564026816; yjs_js_security_passport=76d517a36b6cea24775539304d39f1d5b4a11c3d_1564026815_js",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        }

    # 获取token
    def get_token(self):
        html = requests.get(
            url = self.get_url,
            headers = self.headers
        ).text
        # 正则解析
        pattern = re.compile("token: '(.*?)'",re.S)
        token = pattern.findall(html)[0]

        return token

    # 获取sign
    def get_sign(self,word):
        with open('node.js','r') as f:
            js_data = f.read()
        execjs_obj = execjs.compile(js_data)
        sign = execjs_obj.eval('e("{}")'.format(word))

        return sign

    # 获取翻译结果
    def get_result(self,word,fro,to):
        token = self.get_token()
        sign = self.get_sign(word)
        # 把formdata定义成字典
        formdata = {
            'from': fro,
            'to': to,
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': token,
        }
        html_json = requests.post(
            url = 'https://fanyi.baidu.com/v2transapi',
            data = formdata,
            headers = self.headers
        ).json()

        result = html_json['trans_result']['data'][0]['dst']

        return result



if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    choice = input('1.翻译英语　2.翻译汉语 请选择(1/2):')
    if choice == '1':
        fro = 'en'
        to = 'zh'
    else:
        fro = 'zh'
        to = 'en'

    word = input('请输入要翻译的单词:')
    result = spider.get_result(word,fro,to)
    print(result)























