import os
from http.server import HTTPServer
from dotenv import load_dotenv, find_dotenv

from server.BasicServer import HandleRequests

load_dotenv(find_dotenv())
host = str(os.getenv("SERVER", 'localhost'))
port = int(os.getenv("PORT", 5000))
HTTPServer((host, port), HandleRequests).serve_forever()
