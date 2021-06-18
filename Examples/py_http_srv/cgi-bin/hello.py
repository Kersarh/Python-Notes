#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs
from http.server import HTTPServer, CGIHTTPRequestHandler

print("Content-type: text/html")
print(
    """
<!DOCTYPE HTML>
<html>
<head>
	
	<title>Обработка данных форм</title>
</head>

<body>"""
)
print()
print("<h1>Hello world!</h1>")
