#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 11:07:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """验证测试"""

    def test_cannot_add_empty_list_items(self):
        pass
