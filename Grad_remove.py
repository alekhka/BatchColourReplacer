# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 13:35:29 2016

@author: Alekh
"""


from PIL import Image
import os
k=0;
i=0;
pr=0.0000;
# Loop through all provided arguments

for filename in os.listdir('.'):
    if (filename.endswith('.png')):
         try:
             # Attempt to open an image file
             image = Image.open(filename)
             #image.show()
             i=i+1
             width, height = image.size
             for x in range(width):
                 #print "\n"
                 for y in range(height):
                     p = image.getpixel((x, y))
                     if (p==(116,255,85)) or (p==(255,92,92)) or (p==(255,179,57)) or (p==(160,46,245)) or (p==(255,255,0)) or (p==(3,136,0)) or (p==(183,182,255)) or (p==(221,255,186)) or (p==(143,61,41)) or (p==(143,0,0)) or (p==(255,0,0)) or (p==(255,143,0)) or (p==(162,201,255)) or (p==(128,255,183)) or (p==(18,59,74)) or (p==(124,0,143)) or (p==(181,113,160)) or (p==(91,118,255)) or (p==(79,35,0)) or (p==(82,67,46)) or (p==(255,208,143)) or (p==(203,255,248)) or (p==(255,206,204)) or (p==(81,214,74)) or (p==(143,136,250)) or (p==(0,255,243)) or (p==(60,181,127)) or (p==(250,93,255)) or (p==(130,10,35)) or (p==(0,0,255)) or (p==(255,255,255)):
                         #print p
                         #print " "
                         k = 1
                     else:
                          image.putpixel((x, y), (0, 0, 0))
             
             filename2 = "Image" + str(i) +".png"
             #image.save(filename2)
             image.save(os.path.join('edited',filename2))
             pr= float(i * 10 / 426)
             print pr
        
         except IOError, e:
             # Report error, and then skip to the next argument
             print "Problem opening", filename, ":", e
             continue

