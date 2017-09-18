# circuitpython_neopixel_strip
library for manipulating a strip of NeoPixels 

The code assumes a strand length of 10 pixels.
This may be changed to an input as the library progresses.

requires:
* software:
  * Cirtuit Python (I am using 2.0.x ) 
  * neopixel.mpy (you will likely need to download the zip to get the mpy file from the zip)
    * https://github.com/adafruit/Adafruit_CircuitPython_Bundle
  
  * neopixel.py 
    * https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/tree/1142f1c7fdc232a46d74dd4f1946a5f462ae2555

  * I don't have space for all the libraries on the Feather m0 Bluefruit for all the circuit python libraries so I just added the neopixel.mpy and neopixel.py into a new lib directory on the feather.
  
* hardware:
  * a board that supports circuit python
  * a neopixel strip (I am using a strip of 10 currently so the library currently has this value hardcoded)
