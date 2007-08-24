#!python
# -*- coding: UTF-8 -*-
"""
nabazlib samples: ChoreographySample
A simple Choreography using leds and ears
"""

from nabazlib.Nabaztag import *

if __name__ == '__main__':
  # replace with your nabaztag's id 
  myNabaztag = Nabaztag('0019DB000619', '1173966344')
  # tempo of 1/2 second
  myChoreography = Choreography(2)
  # move ears 90º in opposite directions
  myChoreography.addEarCommand(0, Choreography.EAR_LEFT, 90, Choreography.EAR_BACK)
  myChoreography.addEarCommand(0, Choreography.EAR_RIGHT, 90, Choreography.EAR_FRONT)
  myChoreography.addLedCommand(0, Choreography.LED_TOP, 0, 200, 0)
  # do some "fantastic car"-like effect with the lights
  seqCount = 2
  tempoOffset = 0
  while seqCount > 0:
      myChoreography.addLedCommand(0 + tempoOffset, Choreography.LED_LEFT, 255, 0, 0)
      
      myChoreography.addLedCommand(1 + tempoOffset, Choreography.LED_LEFT, 120, 0, 0)
      myChoreography.addLedCommand(1 + tempoOffset, Choreography.LED_MIDDLE, 255, 0, 0)
      
      myChoreography.addLedCommand(2 + tempoOffset, Choreography.LED_LEFT, 0, 0, 0)
      myChoreography.addLedCommand(2 + tempoOffset, Choreography.LED_MIDDLE, 120, 0, 0)
      myChoreography.addLedCommand(2 + tempoOffset, Choreography.LED_RIGHT, 255, 0, 0)
      
      myChoreography.addLedCommand(3 + tempoOffset, Choreography.LED_MIDDLE, 255, 0, 0)
      myChoreography.addLedCommand(3 + tempoOffset, Choreography.LED_RIGHT, 120, 0, 0)
      
      myChoreography.addLedCommand(4 + tempoOffset, Choreography.LED_LEFT, 255, 0, 0)
      myChoreography.addLedCommand(4 + tempoOffset, Choreography.LED_MIDDLE, 120, 0, 0)
      myChoreography.addLedCommand(4 + tempoOffset, Choreography.LED_RIGHT, 0, 0, 0)
      
      seqCount -= 1
      tempoOffset += 5
  myNabaztag.doChoreography(myChoreography)