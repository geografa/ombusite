#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
sys.path.append('./lib/local')

BUILD_ENV = 'production'
AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
DOMAIN = 'qa2.dev.ombuweb.com'
SITEURL = 'http://' + DOMAIN
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
