import os

myCmd = 'cd Downloads/'
os.system(myCmd)

myCmd = 'arduino-cli board list'
os.system(myCmd)

myCmd = 'arduino-cli compile --fqbn arduino:avr:uno ~/Downloads/Myfirst'
os.system(myCmd)

myCmd = 'arduino-cli upload -p /dev/cu.usbmodem14201 --fqbn arduino:avr:uno ~/Downloads/Myfirst'
os.system(myCmd)

