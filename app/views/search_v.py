import json

from tornado.web import RequestHandler

class SearchHandler(RequestHandler):
    mapper = {
        'python': 'python是目前世界上最流行的AI语言',
        'java': 'java已经是20多年企业级应用开发语言',
        'H5': 'H5全称html5， 与2014年流行的前端web前端语言'
    }

    def get(self):
        html = """
            <h3>搜索%s结果</h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)

        # self.write(html % (wd, result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))

        self.set_status(200)  # 设置响应的状态码
        # 设置响应头的数据类型
        self.set_header('Content-Type', 'application/json;charset=utf-8')

        # 设置cookie操作
        self.set_cookie('wd', wd)
