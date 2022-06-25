#!/usr/bin/env python3

import sys
import os
dirname = os.path.dirname(__file__)
mediadir = os.path.join(dirname,'media')
from waveshare_epd import epd7in5_V2
from PIL import Image,ImageDraw,ImageFont
import csv



#Font cosntants
fontList = ImageFont.truetype(os.path.join(mediadir, 'Font.ttc'), 25)
fontTitle = ImageFont.truetype(os.path.join(mediadir, 'Font.ttc'), 40)



#initialize the display
epd = epd7in5_V2.EPD()
epd.init()
#epd.Clear()


#set up immage and draw items
Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

#Constants for text positions and increments 
YSTART = 110
XSTART = 20
XINC = 50
YINC = 40

#initialize x and y to starting positions
ycord = YSTART
xcord = XSTART

#initialize yadjust to 0 and current/previous positions to 'main'
yadjust = 0
prev = 'main'
curr = 'main'


#Draw the top title graphics
XRSTART = 5
YRSTART = 10
XREND = 795
YREND = 90
draw.rectangle((XRSTART,YRSTART,XREND,YREND))
draw.rectangle((XRSTART +1,  YRSTART + 1,  XREND - 1, YREND - 1))
draw.rectangle((XRSTART +2,  YRSTART + 2,  XREND - 2, YREND - 2))
draw.text((300 , 25), 'To Do List' , font = fontTitle, fill = 0)



# Open the CSV file
with open('todo.csv') as csvfile:
    file  = csv.reader(csvfile,delimiter = ',')
    
    for row in file:
        #determine the current state.  If a sub point then increase xcord
        if int(row[2]) == 0:
            curr = 'main'    
        elif int(row[2]) == 1:
            curr = 'sub'
            xcord = XSTART + XINC
    
        
        # shortens the spacing between main and sub points
        if prev == 'main' and curr == 'sub':
            yadjust = 12     
        elif prev == 'sub' and curr == 'sub':
            yadjust = 12     
        else:
            yadjust = 0
            
            
        #add text to draw object
        draw.text((xcord, ycord - yadjust), row[1].strip() , font = fontList, fill = 0)
         
        #update cordinates.  y increments by contant - some for sub bullets
        #reset x and extray back to std
        #sets prev to current for next loop
        ycord = ycord + YINC - yadjust
        xcord = XSTART
        prev = curr
          
          
        
#display the image then go to sleep to prevent power draw.
epd.display(epd.getbuffer(Himage))
epd.sleep()

