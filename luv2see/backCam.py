import cv2
from PIL import Image
from http.server import BaseHTTPRequestHandler,HTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import io
import socket
import time
import re
import subprocess

import targetingSystem


#extract the ip address (or addresses) from ifconfig
found_ips = []
ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', subprocess.getoutput("/sbin/ifconfig"))
for ip in ips:
  if ip.startswith("255") or ip.startswith("127") or ip.endswith("255"):
    continue
  found_ips.append(ip)

hostName = found_ips[0]
hostPort = 9000


class CamHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            print (self.path)
            if self.path.endswith('.mjpg'):
                self.send_response(200)
                self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
                self.end_headers()
                while(True):# infinite loop with no exit condition
                        rc,img = target.camera.read()
                        if not rc:
                            continue 
                        if rc:
                            #========send img to  the cv_frame() function for CV2 operations======
                            

                            #imgRGB = target.run()
                            #imgRGB = cv_frame(img) # contains all the opencv stuff i want to perform
                            #=============================================================

                            #imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                            r, buf = cv2.imencode(".jpg",imgRGB) 

                            self.wfile.write("--jpgboundary\r\n".encode("utf-8"))
                            self.send_header('Content-type','image/jpeg')
                            self.send_header('Content-length',str(len(buf)))
                            self.end_headers()
                            self.wfile.write(bytearray(buf))
                            self.wfile.write('\r\n'.encode("utf-8"))
                            time.sleep(0.01)

                            k = cv2.waitKey(20)
                            if k == 27: 
                                break



                cv2.destroyAllWindows()
                capture.release()   

                return

            if self.path.endswith('.html') or self.path=="/":
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('<html><head></head><body>'.encode("utf-8"))
                s = '<img src="http://' +socket.gethostbyname(socket.gethostname())+':'+ str(hostPort) +'/' + 'back' + '.mjpg"/>'
                self.wfile.write(s.encode("utf-8"))
                self.wfile.write('</body></html>'.encode("utf-8"))
                return





def main():

    global target, capture, average

    target = targetingSystem.TargetingSystem( 0, 100, 255 )


    while(1):

        server1 = HTTPServer((hostName,hostPort),CamHandler)
        print ("servers started on: ", hostName)


        k = cv2.waitKey(20)

        try:
            server1.serve_forever()
        except KeyboardInterrupt:
            server1.socket.close() 
            print("server stopped")
            break
    return



main()