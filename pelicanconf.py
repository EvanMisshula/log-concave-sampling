AUTHOR = 'columbia-ot-reading-group'
SITENAME = 'log-concave-sampling'
SITEURL = ""

PATH = "content"
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('ambition','/pages/ambition.html'),
             ('background','/pages/background.html'),
             ('contact','/pages/contact.html'),
]

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_LANG = u'en'
STATIC_PATHS = [ 'images']
IGNORE_FILES = ['.#*', '*~']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
 'extensions': [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.meta',
        'markdown.extensions.sane_lists',
        'markdown.extensions.toc',
        'markdown.extensions.smarty',
        'markdown.extensions.nl2br',
        'markdown.extensions.admonition',
        'markdown.extensions.attr_list',
    ],
    'output_format': 'html5',
}



# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# # Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
