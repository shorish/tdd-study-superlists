from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.models import Item

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

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # self.assertIn('A new list item', response.content.decode('utf-8'))
        # self.assertTemplateUsed(response, 'home.html')

    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/')

    def test_redirect_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

# class SmokeTest(TestCase):
#     """docstring for SmokeTest"""

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

    def test_displays_all_list_items(self):
        # 设置
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        # 使用
        response = self.client.get('/')

        # 断言
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
