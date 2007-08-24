#!python
# -*- coding: UTF-8 -*-
"""
nabazlib samples: HelloWorldSample
You need this one }:)
"""

from nabazlib.Nabaztag import Nabaztag

if __name__ == '__main__':
  # replace with your nabaztag's id 
  myNabaztag = Nabaztag('0019DB000619', '1173966344')
  # a simple say
  print "Sending a Hello World!"
  myNabaztag.say("Hello World!")
