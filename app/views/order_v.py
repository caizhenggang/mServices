from tornado.web import RequestHandler


class OrderHandler(RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'python高级开发',
            'author': 'disen',
            'price': 190
        },
        {
            'id': 2,
            'name': 'python3 vs python2',
            'author': 'disen',
            'price': 290
        },
    ]
    action_map = {
        1: '取消订单',
        2: '在此购买',
        3: '评价'
    }

    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        print('-----initialize----------')

    def prepare(self):
        # 在初始化之后，调用行为方法之前，
        # 调用此方法进行预处理
        print('-------prepare------')

    def get(self, order_id, action_code):
        print('----get------')
        self.write('订单查询')
        html = """
            <p>
                商品编号: %s
            </p>
            <p>
                商品名称: %s
            </p>
            <p>
                商品价格: %s
            </p>
        """
        goods = self.query(int(order_id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(action_code)))

    def post(self, action_code, order_id):
        print('--post----')
        self.write('----post-------')

    def on_finish(self):
        # 在请求处理完成后，释放资源的方法，在行为方法完成后调用
        print('---finish-----')
