from http.server import HTTPServer, BaseHTTPRequestHandler
  
class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content_type','text/html')
        self.end_headers()
        self.wfile.write('Hello world!'.encode())


def main():
    Port = 8000
    server = HTTPServer(('',Port),helloHandler)
    print('server running on port %s' % Port)
    server.serve_forever()


if __name__ == '__main__':
    main()
