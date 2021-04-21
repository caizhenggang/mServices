from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://localhost:9000'

    def test_index_get(self):
        url = self.base_url + '/'
        # 发起get请求，
        # 查询参数 params
        resp = requests.get(url, params={
            'wd':'disen',
            'title':20
        })
        # 可能会出现 400错误： 原因是查询参数没有给对
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/?wd=python'
        # 发起post请求，表单参数使用data来进行指定
        # body 参数
        resp = requests.post(url, data={
            'name':'disen',
            'city':'西安'
        })
        print(resp.text)

class TestCookieRequest(TestCase):
    url = 'http://localhost:9000/cookie'
    def test_search(self):
        resp = requests.get('http://localhost:9000/search', params={
            'wd':'python'
        })
        print(resp.text)
        print(resp.cookies)
        for key,value in resp.cookies.items():
            print(key,value)

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.url, params={
            'name':'session'
        })
        print(resp.text)

class TestOrderRequest(TestCase):
    url = 'http://localhost:9000/order/1/2'
    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)

class TestUserRequest(TestCase):
    url= 'http://localhost:8000/user'
    def test_login(self):
        # 上传了json数据
        resp = requests.get(self.url,
                            json={
                                'name':'disen',
                                'pwd':'123'
                            })
        # 读取响应的json数据
        print(resp.json())
