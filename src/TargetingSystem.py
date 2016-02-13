#!/usr/bin/python3.5

import numpy as np
import cv2 as cv
import sys
import math

# ===========================================================================
# Targeting System Class
# ===========================================================================

class TargetingSystem(object):

  def __init__( self, cam_usb=0, min_val=227, max_val=255 ):
    #Set up camera
    self.camera = cv.VideoCapture( cam_usb )
    
    #Set up threhold values
    self.min      = min_val
    self.max      = max_val

    #Other important stuff that we'll just initialize
    self.frame    = None
    self.thresh   = None
    self.rect     = None
    self.box      = None
    self.contours = None
    self.midpoint = None
    self.theta    = None

  def __del__( self ):
    #Free the camera
    self.camera.release()
    cv.destroyAllWindows()
  
  def set_min( self, val=227 ):
    self.min = val

  def set_min( self, val=255 ):
    self.max = val

  def nextFrame( self ):
    n, self.frame  = self.camera.read()

  def thresholdFrame( self ):
    gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
    
    n, self.thresh = cv.threshold(gray, self.min, self.max, cv.THRESH_BINARY)
    
  def findContours( self ):
    n, self.contours, h = cv.findContours(self.thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cntr in self.contours:
        self.rect = cv.minAreaRect( cntr )
        self.box = cv.boxPoints( self.rect )
        self.box = np.int0( self.box )
        cv.drawContours( self.frame, [ self.box ], 0, (0,0,255), 2)

        self.box = sorted(self.box, key=lambda point:point[1])
        topLeft = self.box[0]
        topRight = self.box[1]

        self.midpoint = ( int((topLeft[0]+topRight[0])/2), int((topLeft[1]+topRight[1])/2) )

        cv.circle( self.frame, self.midpoint, 5, (0,255,0), thickness=2, lineType=8, shift=0 )
        self.getTheta()  

  def showFrame( self ):
    cv.imshow( 'frame', self.frame )

  def getTheta( self ):
    topLeft  = self.box[0]
    topRight = self.box[1]

    x_off = abs(topLeft[0]-topRight[0])
    y_off = abs(topLeft[1]-topRight[1])

    self.theta = math.degrees(math.atan(y_off/x_off))

    cv.putText(self.frame, str(self.theta), (self.midpoint[0]+5, self.midpoint[1]+5), 1, 1.0, (0,255,0))

  def centroid( self ):
    None

  def run( self ):
    #Procedure

    #get next frame from camera feed
    self.nextFrame()

    #threshold the image
    self.thresholdFrame()

    #find and draw contours
    self.findContours()

    #show the frame
    self.showFrame()


def Usage():
    print("Usage: ")
    print("./TargetingSystem <CAMERA USB PORT> <THRESHOLD MIN> <THRESHOLD MAX>")

if __name__ == '__main__':
  if len( sys.argv ) < 2 :
    Usage()
  else:
      print("Starting Targeting System...")
      if len( sys.argv ) < 3 :
        usb = int(sys.argv[1])
        ts  = TargetingSystem( cam_usb=usb )
      else:
        usb = int(sys.argv[1])
        mn  = int(sys.argv[2])
        mx  = int(sys.argv[3])
        ts  = TargetingSystem( cam_usb=usb, min_val=mn, max_val=mx )

      while(True):
        ts.run()
        if cv.waitKey(1) & 0xFF == ord('q'):
          break
      del ts
