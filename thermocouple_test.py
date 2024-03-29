#!/usr/bin/python
# Copyright (c) 2015 Michael Leibowitz
# Copyright (c) 2014 Adafruit Industries
# Original Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0


# Raspberry Pi software SPI configuration.
CLK = 11
CS  = [16, 20, 21]
DO  = 9
sensors = []
for cs in CS:
        sensors.append(MAX31855.MAX31855(CLK, cs, DO))
# Loop printing measurements every second.
print 'Press Ctrl-C to quit.'
while True:
        for idx, sensor in enumerate(sensors):
                temp = sensor.readTempC()
                internal = sensor.readInternalC()
                print "thermocouple %d" % idx
                print '  Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp))
                print '  Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal))
        print ""
        time.sleep(1.0)
