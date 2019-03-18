import urllib.request
import os
from random import *

## Creates a directory of html files
if not os.path.exists("html_files"):
	os.mkdir("html_files")

i = 2
# while i = 1:
#     print(i)
file_name = "html_files/boardgame_{}.html".format(i)
print(file_name)
f = open(file_name, "wb")
url = "https://boardgamegeek.com/browse/boardgame/page/{}".format(i)
print(url)
response = urllib.request.urlopen(url)
html = response.read()
f.write(html)
f.close()
