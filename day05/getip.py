import requests

def get_ip_list():
    api_url = 'http://dev.kdlapi.com/api/getproxy/?' \
              'orderid=926382819150419&num=100&protocol=' \
              '2&method=2&an_an=1&an_ha=1&sep=1'
    html = requests.get(url=api_url).text
    ip_port_list = html.split('\r\n')

    # ip_port_list: ['IP:PORT','IP:PORT']
    return ip_port_list

if __name__ == '__main__':
    print(get_ip_list())





















