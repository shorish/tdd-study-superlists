from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """docstring for HomePageTest"""

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # 方法一：手动获取html内容判断模板是否渲染正确
        # request = HttpRequest()
        # response = home_page(request)
        # 创建HttpRequest对象，调用视图对象函数
        # 或调用self.client.get访问需要测试的URL
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        '''test_home_page_returns_correct_html可精简为本方法'''
        # 方法二：调用Django TestCase类提供的测试方法，assertTemplateUsed检查是否使用指定模板渲染
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


# class SmokeTest(TestCase):
#     """docstring for SmokeTest"""

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)
