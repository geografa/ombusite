#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
sys.path.append('./lib/local')

BUILD_ENV = 'production'
AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False
THEME = 'theme'
PATH = 'src'
STATIC_PATHS = ['images']
FEED_ATOM = None
FEED_RSS = None
WEBASSETS = True
DIRECT_TEMPLATES = ('index',)
GOOGLE_ANALYTICS = 'UA-16055309-1'

from custom_filters import cdn
JINJA_FILTERS = {'cdn': cdn}
