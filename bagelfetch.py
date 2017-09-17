#!/usr/bin/python
import urllib
url = "http://rawgit.com/monthlybagelco/monthlybagel/master/bagel.html"
f = urllib.urlopen(url)
print f.read()