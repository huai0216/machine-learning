# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:21:50 2022

@author: huai
"""
import math
try:
  radius = float(input("radius: "))
  if(radius <= 0):
    print("Please enter a positive number")
  else :
    y = 2*math.pi*radius
    z = math.pi * (radius)**2
    print("圓半徑為{0},圓周長為{1},圓面積為{2}".format(radius, y, z))
except ValueError:
  print("Please enter a positive number")