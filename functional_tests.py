#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 11:07:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """新访问者测试"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 访问应用的首页
        self.browser.get('http://localhost:8000')
        # 网页的标题和头部都包含To-do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # 她在文本框输入了”Buy peacock feathers“
        inputbox.send_keys("Buy peacock feathers")

        # 按回车后页面更新了
        # 待办事项表格显示了”1: Buy peacock feathers“
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        # 页面又显示了一个文本框，可以输入其他待办事项
        # 她接着输入其他

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
