import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
        
if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())# Generateas a random string, learning                                  # how diff urls lead to diff functions.

import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
    
    @cherrypy.expose
    def generate(self):
        return ''.join(random.samplel(string.hexdigits, 8))
    
if __name__ =='__main__':
    cherrypy.quickstart(StringGenerator())
    
'''(From tutorial at docs.cherrypy.org) Go now to http://localhost:8080/generate and your browser will display a random string.

Let’s take a minute to decompose what’s happening here. This is the URL that you have typed into your browser: http://localhost:8080/generate

This URL contains various parts:

http:// which roughly indicates it’s a URL using the HTTP protocol (see RFC 2616).
localhost:8080 is the server’s address. It’s made of a hostname and a port.
/generate which is the path segment of the URL. This is what CherryPy uses to locate an exposed function or method to respond.
Here CherryPy uses the index() method to handle / and the generate() method to handle /generate'''