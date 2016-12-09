#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Lindsay'
SITENAME = u'Ben Lindsay'
OUTPUT_PATH = 'output/'
SITEURL = ''

# Settings in http://simblestudios.com/blog/development/pages-as-pelican-top-level.html

# # put articles (posts) in blog/
# ARTICLE_URL = 'blog/{slug}.html'
# ARTICLE_SAVE_AS = 'blog/{slug}.html'
# # we need to change the main index page now though...
# INDEX_SAVE_AS = 'blog/index.html'
# INDEX_URL = 'blog/'
# #now move all the category and tag stuff to that blog/ dir as well
# CATEGORY_URL = 'blog/category/{slug}.html'
# CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
# CATEGORIES_URL = 'blog/category/'
# CATEGORIES_SAVE_AS = 'blog/category/index.html'
# TAG_URL = 'blog/tag/{slug}.html'
# TAG_SAVE_AS = 'blog/tag/{slug}.html'
# TAGS_URL = 'blog/tag/'
# TAGS_SAVE_AS = 'blog/tag/index.html'
# ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
# ARCHIVES_URL = 'blog/archives/archives.html'
# AUTHOR_SAVE_AS = 'blog/{slug}.html'
# AUTHORS_SAVE_AS = 'blog/authors.html'
# # put pages in the root directory
# PAGE_SAVE_AS = '{slug}.html'
# PAGE_URL = '{slug}.html'

# put articles (posts) in blog/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'index.html'
INDEX_URL = ''
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
# put pages in the root directory
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud']

STATIC_PATHS = ['js', 'css', 'images']

TAG_CLOUD_STEPS = 50
TAG_CLOUD_MAX_ITEMS = 20
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_BADGE = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
MENUITEMS = [('Blog', '/blog/'), ('Projects', '/projects/')]
THEME = "theme"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/benlindsay'),
          ('LinkedIn', 'https://www.linkedin.com/in/benjlindsay'),)

DISQUS_SITENAME = 'benlindsay'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
