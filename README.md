# TwoDigitGrid

This Python module contains a single function (numToMatrix) which creates a 64 element list
designed to be used as an image for the Astro-PI HAT LED  [Astro-Pi] (http://astro-pi.org/hardware/) HAT LED matrix.

###Usage

Make sure TwoDigitGrid is in your working directory

\>\>\> import TwoDigitGrid as TDG

\>\>\> image = TDG.numToMatrix(24,back_colour=[0,0,0],text_colour=[255,0,0])

\>\>\> image

[[0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0]]


###AstroPi Example

\>\>\> import TwoDigitGrid as TDG

\>\>\> from astro_pi import AstroPi

\>\>\> ap = AstroPi()

\>\>\> image = TDG.numToMatrix(24,back_colour=[0,0,0],text_colour=[255,0,0])

\>\>\> ap.set_pixels(image)

###Installation

1. Clone this repo

See my [blog] (http://richardhayler.blogspot.com/) for  updates and other Raspberry Pi projects.