"""
webframe.py
用于模拟网站后端应用工作流程
"""
from socket import *
import json
from settings import *
from select import *
from urls import *  #导入路由
# frame的绑定地址
frame_address = (frame_ip, frame_port)


# 网站应用类
class Application:
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(frame_address)
        self.ep = epoll()  # 生成epoll对象
        self.fdmap = {}  # 查找字典

    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % frame_port)
        self.ep.register(self.sockfd, EPOLLIN)  # 关注epollin
        self.fdmap[self.sockfd.fileno()] = self.sockfd
        while True:
            events = self.ep.poll()
            for fd, event in events:
                if fd == self.sockfd.fileno():
                    connfd, addr = self.fdmap[fd].accept()
                    self.ep.register(connfd, EPOLLIN | EPOLLET)  # 边缘触发
                    self.fdmap[connfd.fileno()] = connfd
                elif event & EPOLLIN:
                    self.handle(self.fdmap[fd])  # 处理http请求
                    self.ep.unregister(fd)
                    del self.fdmap[fd]

    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request-->{'method':'GET','info':'/'}
        # print(request)  测试连通
        # data=json.dumps({'status':'200','data':'ccccc'})
        # connfd.send(data.encode())
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])  # 返回data是数据字典
        elif request['method'] == 'POST':
            pass
        #将response发送给httpserver
        response=json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self,info):
        if info=='/':
            filename=STATIC_DIR+'/index.html'
        else:
            filename=STATIC_DIR+info
        try:
            fd=open(filename)
        except Exception:
            f=open(STATIC_DIR+"/404.html")
            return {'status':'404','data':f.read()}
        else:
            return {'status': '200', 'data':fd.read()}


    #请求数据处理   info-->/time
    def get_data(self,info):
        #urls-->[('/time',time),(),()]
        for url,fun in urls:
            if url==info:
                return {'status':'200','data':fun()}
        return {'status': '404', 'data': 'Sorry......'}
app = Application()
app.start()  # 启动服务
