#!/usr/bin/env python3
#encoding=UTF-8
import math
import logging
def fib(max):
    #斐布数列
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

class Vector:
    # a 3d vector
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.length = math.sqrt(x*x+y*y+z*z)

    def set(self,v:dict):
        self.x = v.x;
        self.z = v.y;
        self.z = v.z;
        self.length = math.sqrt(v.x*v.x+v.y*v.y+v.z*v.z)

def tranLower(s):
  if isinstance(s,str):
    return s.lower()
  else:
    return ''

def triangles(max):
  floor = [1]
  while len(floor)<max:
    yield floor;
    temp = list(range(len(floor)+1))
    i = 0
    for x in temp:
      if i == 0:temp[0] = 1;
      elif i == len(temp)-1:temp[i] = 1;
      else:temp[i] = floor[i]+floor[i-1];
      i += 1
      pass;
    floor = temp





