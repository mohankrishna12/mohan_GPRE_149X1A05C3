import urllib

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5,GPIO.OUT)
url="http://pavanlight.000webhostapp.com/buttonStatus.txt"
while(True):

                try:

                        html = urllib.urlopen(url).read()
                        if html=='off':
                             GPIO.output(5,False)


                             print html
                        elif html=='on':
                             GPIO.output(5,True)
                             print html


                except :
                        print "error occured"

input()                                
                                

