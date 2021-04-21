from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        self.write('<h3>Hello, Tornado</h3>')


if __name__ == '__main__':
    # 创建web应用
    app = Application([
        ('/', IndexHandler)
    ])
    # 绑定端口
    app.listen(7000)
    # 启动服务
    print('start http://localhost: %s' % 7000)
    IOLoop.current().start()