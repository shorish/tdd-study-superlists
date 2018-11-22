#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 11:07:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from .base import FunctionalTest
# class NewVisitorTest(unittest.TestCase):
# class NewVisitorTest(LiveServerTestCase):


class LayoutAndStyleingTest(FunctionalTest):
    """布局样式测试"""

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            270,
            delta=25
        )
