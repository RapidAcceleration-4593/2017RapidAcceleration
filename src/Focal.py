#!/usr/bin/python3.5

import numpy as np
import cv2 as cv
import sys
import math

# ===========================================================================
# Targeting System Class
# ===========================================================================

class Focal(object):

  def __init__( self ):
    #ALL MEASUREMENTS ARE IN METERS
    self.focal_length = None

    #This should never change once we know this
    self.known_pixel_width = 361

    #This will never change
    self.known_real_width = 0.3556

    #This will never change
    self.known_real_distance = 0.9144

    #This will change every single frame
    self.current_pixel_width = None

    #This is what we want
    self.actual_real_distance = None



  def __del__( self ):
    pass
  
  def setFocalLength( self ):
    ratio = ( self.known_real_distance / self.known_real_width )
    self.focal_length = self.known_pixel_width * ratio

  def CalculateActualDistance( self ):
    ratio = self.focal_length / self.current_pixel_width
    self.actual_real_distance = self.known_real_width * ratio

  def CalculateCurrentPixelWidth( self ):
    #read frame from image

    #find left side of contours

    #find right side of contours

    #calculate distance

    #return pixel width

  def getDistance( self );
    return self.actual_real_distance


def Usage():
    print("Usage: ")
    #print("./Focal <KNOWN_OBJECT_DISTANCE> <KNOWN_PIXEL_DISTANCE> <THRESHOLD MAX>")

if __name__ == '__main__':
  f = Focal( )
  f.setFocalLength( )
  f.CalculateCurrentPixelWidth( )
  f.CalculateActualDistance( )
  print( f.getDistance( ) )
