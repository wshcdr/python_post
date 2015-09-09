from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print post_data
		
		decoded = json.loads(post_data)
		print decoded['a']

server = HTTPServer(('', 1111), RequestHandler)
server.serve_forever()