#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
sys.path.append('./lib/local')

AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
SITEURL = 'http://ombuweb.com'
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False
THEME = 'theme'
PATH = 'src'
STATIC_PATHS = ['images']
FEED = None
WEBASSETS = True

from custom_filters import cdn
JINJA_FILTERS = {'cdn': cdn}
