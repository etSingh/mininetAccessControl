import SimpleHTTPServer
import SocketServer
import logging
import cgi
import sys

PORT = 80
noOfIp = 0

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        myStri = ""
        logging.error(self.headers)
        
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        with open("test.txt", "a") as myfile:
             ip = (form.getvalue('output'))
             print "the ip is", ip 
             global noOfIp
             print "noOfIp=", noOfIp
             x = noOfIp
             noOfIp = len(ip)
             if (isinstance(ip, basestring)):
                myfile.write(ip.strip() + "\n")
             else:
                for i in range(noOfIp):
                    myfile.write(ip[i] + "\n")

                
        

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)


httpd.serve_forever()
