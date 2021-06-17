import datetime
import xml.sax.saxutils

COPYRIHT_TEMPLATE = 'Copyright (c) {0} {1} All rights reserved.'
STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css" '
                            'media="all" href="{0}" />\n')
HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<! {copyright} >
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta equiv="contenttype" content="text/html; charset=utf8" />
{stylesheet}\
</head>
<body>
</body>
</html>
"""

class CancelledError(Exception): pass

def main():
    information = dict(name=None, year=datetime.date.today().year,
                       filename=None, title=None, description=None,
                       keywords=None, stylesheet=None)
    while True:
        try:
            print('\n Make HTML Skeleton \n')
            collect_inf(information)
            create_skeleton(**information)
        except CancelledError():
            print('Cancelled')
        if (get_string('\n Create another (y/n)? [{0}]: \n', default='y').lower()
            not in {'y','yes'}):
            break
        
def collect_inf(information):
    name = get_string('Enter your name (for copyright)', 'name',
                      information['name'])
    if not name:
        raise CancelledError()
    year = get_int('Enter copyright year', 'year',
                      information['year'], 2000,
                      datetime.date.today().year +1, True)
    if year== 0:
        raise CancelledError()
    filename = get_string("Enter filename", "filename")
    if not filename:
        raise CancelledError()
    if not filename.endswith((".htm", ".html")):
        filename += ".html"
    title = get_string('Enter title: ', 'title')
    if not title:
        raise CancelledError()
    description = get_string("Enter description (optional)",
                             "description")
    keywords = []
    while True:
        keyword = get_string('Enter a keyword', 'keyword')
        if keyword:
            keywords.append(keyword)
        else:
            break
    stylesheet = get_string('Enter the stylesheet filename (optional)',
                            'stylesheet')
    if stylesheet and not stylesheet.endswith('.css'):
        stylesheet += '.css'
    information.update(name=name, year=year, filename=filename, title=title,
                       description=description, keywords=keywords,
                       stylesheet=stylesheet)

def get_string(msg, name='string', default=None, min_length=0, max_length=80):
        msg += ': ' if default is None else '[{0}]: '.format(default)
        
    
            
