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

    #This is what we want
    self.actual_real_distance = None



  def __del__( self ):
    pass
  
  def setFocalLength( self ):
    ratio = ( self.known_real_distance / self.known_real_width )
    self.focal_length = self.known_pixel_width * ratio

  def calculateActualDistance( self, current_pixel_width ):
    if current_pixel_width != 0:
      ratio = self.focal_length / current_pixel_width
      self.actual_real_distance = self.known_real_width * ratio
    else:
      self.actual_real_distance = 9999;

  def getDistance( self ):
    return self.actual_real_distance


def Usage():
    print("Usage: ")
    #print("./Focal <KNOWN_OBJECT_DISTANCE> <KNOWN_PIXEL_DISTANCE> <THRESHOLD MAX>")

if __name__ == '__main__':
  f = Focal( )
  f.setFocalLength( )
  f.CalculateActualDistance( )
  print( f.getDistance( ) )
