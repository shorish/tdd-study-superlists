#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 11:07:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
