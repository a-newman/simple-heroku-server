#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    python3 server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import traceback
import os
import shutil
import json
import uuid
from enum import Enum
from save_data import save_locally, save_mongo

class SaveMethod(Enum): 
    LOCAL = save_locally
    MONGO = save_mongo

SAVE_METHOD = SaveMethod.LOCAL
COUNTER = "server/counter.txt"
INDEX = "index.html"

def get_querystring(path): 
    """
    A helper function that takes in a url and returns the query string as
    a dictionary. 

    For instance, given a website like "google.com?query=pugs", this function
    will return the dictionary {'query': 'pugs'}
    """
    pairs = {}
    qstring = path.split('?')
    if len(qstring) == 1: 
        return {} 
    else: 
        qstring = qstring[-1]   
    path = qstring.split('&')
    for pair in path: 
        key, val = pair.split('=')
        pairs[key] = val
    return pairs

def strip_qstring(path): 
    """
    A helper function that removes the query string from a url. 
    
    For instance, given a url like "google.com?query=pugs", returns 
    "google.com".
    """
    p = path.split('?')
    if len(p) == 1: 
        return path
    return "".join(p[:-1])

class S(SimpleHTTPRequestHandler):
    """ 
    Class for handling an HTTP request. 
    """
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _copyfile(self, source, dest): 
        shutil.copyfileobj(source, dest);

    def do_GET(self):
        print("GETTING")
        base_path = strip_qstring(self.path)
        try:
            if (base_path == '/counter'): 
                self._set_headers()
                with open(COUNTER, 'r+') as infile: 
                        counter = int(infile.read().strip())
                        infile.seek(0)
                        infile.write(str(counter + 1))
                self.wfile.write(str(counter).encode())
                return
            else: 
                # override the default behavior of the simple handler
                super(S, self).do_GET()
        except Exception as e: 
            traceback.print_exc()
            self.send_error(500, "Internal server error: {}".format(e))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Post request to save data
        try: 
            if (self.path == "/data"): 
                self._set_headers()
                data = self.rfile.read(int(self.headers['Content-Length']))
                data = data.decode("utf-8")
                data = json.loads(data)
                print("DATA", data)
                key = str(uuid.uuid4())
                SAVE_METHOD(key, data)
                print("SAVED DATA")
                response = json.dumps({'key': key})
                self.send_response(200)
                self.wfile.write(response.encode())
            else: 
                self.send_error(400, "Page does not exist")
        except Exception as e: 
            traceback.print_exc()
            self.send_error(500, "Internal server error: {}".format(e))
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    # Get the environment variable PORT
    environ_port = os.environ.get('PORT')
    # TODO: if environ_port is not NONE, convert it to an int and set
    # `port` to that int, so that this will run correctly on Heroku.
    # Your code here
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
