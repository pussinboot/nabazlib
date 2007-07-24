#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Nabaztag python API tests
by Ricardo Varela <phobeo@gmail.com>

This module tests the API provided in Nabaztag.py
"""

import unittest
import com.phobeo.nabazlib
    
class ChoreographyTest(unittest.TestCase):
    """ Tests for the Choreography helper class """
    
    def testExceptionEmpty(self):
        empty = Choreography()
        self.assertRaises(ValueException, empty.buildChoreography())
        
    def testSetTempo(self):
        ch = Choreography()
        ch2 = Choreography(30)
        self.assertEquals(ch.tempo, 10)
        self.assertEquals(ch2.tempo, 30)
    
    def testSimpleEar(self):
        ch = Choreography()
        ch.addEarCommand(0, Choreography.EAR_LEFT, 20, Choreography.EAR_BACK)
        self.assertEquals(ch.buildChoreography(), "10,0,motor,1,20,0,0")
    
if __name__ == '__main__':
    unittest.main()
    
        
    