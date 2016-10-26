#!/bin/bash
#script to set correct touchscreen orientation after x start
#this won't rotate the displayed image, only the touchscreen input
#to rotate the displayed image add the following to /boot/config.txt
#"display_rotate=1" to rotate display 90 degrees
#"display_rotate=3" to rotate display 270 degrees

xinput set-prop 'FT5406 memory based driver' 'Evdev Axes Swap' 1

#Uncomment this for 90 rotation
#xinput --set-prop 'FT5406 memory based driver' 'Evdev Axis Inversion' 0 1

#Uncomment this for 270 rotation
xinput --set-prop 'FT5406 memory based driver' 'Evdev Axis Inversion' 1 0