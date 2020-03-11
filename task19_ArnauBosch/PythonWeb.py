from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

HOST_ADDRESS = "localhost"
HOST_PORT = 8073

class RequestHandler(BaseHTTPRequestHandler):
    """ Our custom, example request handler """
    def do_GET(self):
        """ response for a GET request """

        if "practica.html" in self.path:
            
            file = open('practica.html','rb')
            self.send_response(200)

            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(file.read())
            

        else:
            self.send_error(404,"nO eNCuEntRo lA pAgiNa jUliO :v")
        
     
  
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """ follows example shown on docs.python.org """
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)