#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#PLUGINS = ['pelican_youtube']

AUTHOR = u'Devin Schwab'
SITENAME = u'Devin Schwab'
SITEURL = 'http://devinschwab.com'

PATH = 'content'
STATIC_PATHS = ['pdfs']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = None

DEFAULT_PAGINATION = False

THEME = 'themes/gum'

# Theme variables
GITHUB_URL = 'http://github.com/rhololkeolke'
TWITTER_URL = 'http://twitter.com/rhololkeolke'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
