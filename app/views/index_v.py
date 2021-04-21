from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        # 请求参数的读取
        # 1.读取单个参数
        wd = self.get_argument('wd')
        print(wd)
        # 2. 读取多个参数名相同的参数值
        titles = self.get_arguments('title')
        print(titles)
        # 3. 从查询参数中读取URL路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments('title')
        print(titles2)

        # 4.从请求对象中读取参数
        rep: HTTPServerRequest = self.request
        # request 请求中的数据都是dict字典类型
        wd3 = rep.arguments.get('wd')
        print(wd3)  # 字典key对应的value值都是bytes字节类型

        wd4 = rep.query_arguments.get('wd')
        print(wd4)
        self.write('<h2>我是主页</h2>')

    def post(self):
        # 新增数据
        # 读取表单参数
        # name = self.get_argument('name')
        # city = self.get_argument('city')

        # 建议使用以下方式
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')

        wd = self.get_query_argument('wd')

        self.write('<h2>我是post请求方法: %s %s %s</h2>' % (name, city, wd))

    def put(self):
        self.write('<h2>我是put请求方法</h2>')

    def delete(self):
        self.write('<h2>我是delete请求方法</h2>')