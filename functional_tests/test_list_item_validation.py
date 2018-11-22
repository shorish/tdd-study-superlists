#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 11:07:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


# from unittest import skip

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    """验证测试"""

    def test_cannot_add_empty_list_items(self):
        # 访问首页，没输入内容就按回车
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # 首页显示一个错误信息
        self.wait_for(lambda:
                      self.assertEqual(
                          self.browser.find_element_by_css_selector('.has-error').text,
                          "You can't have an empty list item"
                      ))

        # 输入一些文字，再次提交，这次没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 又提交一个空行，还是报错
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda:
                      self.assertEqual(
                          self.browser.find_element_by_css_selector('.has-error').text,
                          "You can't have an empty list item"
                      ))

        # 输入一些文字，再次提交，这次没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

        self.fail('finish this test!')
