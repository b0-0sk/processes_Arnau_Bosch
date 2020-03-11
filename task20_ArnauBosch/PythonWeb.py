from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
#SMTP SSL
import smtplib, ssl


HOST_ADDRESS = "192.168.2.127"
HOST_PORT = 8073 # For SSL






class RequestHandler(BaseHTTPRequestHandler):
    """ Our custom, example request handler """
    def do_GET(self):
        """ response for a GET request """

        if "baixa.png" in self.path:
            
            file = open('baixa.png','rb')
            self.send_response(200)

            self.send_header("Content-type","image/png")
            self.end_headers()
            self.wfile.write(file.read())
            
            # Method to send email
            sendEmail(self.client_address)
            

        else:
            self.send_error(404,"nO eNCuEntRo lA pAgiNa jUliO :v")
        
     
  
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """ follows example shown on docs.python.org """
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def sendEmail(addr):
    
    # SMTP configuration
    port = 465 # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "formatodiversion@gmail.com" # sending address
    receiver_email = "formatodiversion@gmail.com"  # receiver address
    password = "Casi crack"   # password
    message = "Subject: Hi there"+ "\n\n\nThe address " + str(addr) + """ has visited the image.""" # Email content data
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.ehlo()  # Greeting message with another mail server
        server.login(sender_email, password) # Login
        server.sendmail(sender_email, receiver_email, message) # Send image

if __name__ == '__main__':
    run(handler_class=RequestHandler)