#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

# TODO : Theme puts the author's name below the logo, should put sitename (i.e.
# it assumes this is a blog).
AUTHOR = 'Jason K. Moore'
SITENAME = 'Special Topics in<br> Sports Engineering'
SITEURL = ''
SOURCEURL = 'https://github.com/moorepants/me41035'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# This sets the default pages to be top level items and articles to be under
# /blog/.
INDEX_SAVE_AS = 'blog/index.html'

# All blog posts will have slugs that match the file name.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'  # regex to grab file name without ext
ARTICLE_URL = 'blog/{path_no_ext}.html'
ARTICLE_SAVE_AS = 'blog/{path_no_ext}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'

#MENUITEMS = [('Blog', '/blog/')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

try:
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ''
else:
    print('Loaded theme and plugins from local config file.')
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']

## THEME

# Alchemy theme settings
#DISQUS_SITENAME = ""
SITESUBTITLE = 'ME41035 2023 Q4'
SITEIMAGE = 'https://moorepants.info/mechmotum-bucket/cyclist-sketch-john-hart.png'
# INSTITUTEIMAGE should be 100px in height
#INSTITUTIONIMAGE = 'https://moorepants.info/mechmotum-bucket/tu-delft-logo-233x100.png'
DESCRIPTION = ''
# pelican-alchemy removed the original theme.css, so bring it back.
THEME_CSS_OVERRIDES = ['theme/css/origtheme.css']
REPO_URL = 'https://github.com/moorepants/me41035'

#GOOGLE_ANALYTICS = ''
#DISQUS_SITENAME = ''

## PLUGINS

PLUGINS = ['render_math', 'extract_toc']
