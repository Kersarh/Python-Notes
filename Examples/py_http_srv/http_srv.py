# -*- coding: UTF-8 -*-

import sys
import codecs
from http.server import HTTPServer, CGIHTTPRequestHandler

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
