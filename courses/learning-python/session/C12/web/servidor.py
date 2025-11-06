import os, sys_details
from http.server import HTTPServer, CGIHTTPRequestHandler

webDir = '.'
port = 80


os.chdir(webDir)
srvAddr = ("", port)
srvObj = HTTPServer(srvAddr, CGIHTTPRequestHandler)

print('Iniciando servidor de web en el puerto: ' + str(port))

srvObj.serve_forever()