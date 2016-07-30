#!/usr/bin/python3
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
url = 'https://www.python.org/events/python-events/'
with request.urlopen(url) as f:
	data = f.readlines()
	print(data)
'''parser.feed(data)'''
