#!/usr/bin/python3
import urllib.request
txt = ""
url = "https://raw.githubusercontent.com/monthlybagelco/monthlybagel/master/bagel.html"
f = urllib.request.urlopen(url)
txt = txt + f.read().decode("utf-8")
print(txt)