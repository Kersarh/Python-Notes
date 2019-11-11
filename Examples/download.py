# -*- coding: utf-8 -*-

import urllib.request
logo = urllib.request.urlopen(
    """https://yastatic.net/iconostasis/_/8lFaTHLDzmsEZz-5XaQg9iTWZGE.png"""
).read()
f = open("image.jpg", "wb")
f.write(logo)
f.close()
