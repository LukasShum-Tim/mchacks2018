# -*- coding: utf-8 -*-

from PIL import Image
import os
import image_slicer
import io 
from mchacks_fnc import*
from sklearn.externals import joblib
"""foo = training("C:/pythonfiles/mchacks/guns", "C:/pythonfiles/mchacks/non_guns")

boo = predict(foo, "C:/pythonfiles/mchacks")"""

#dirname=os.chdir("C:/pythonfiles/mchacks")
directory_path="C:/pythonfiles/mchacks"
there_images="C:/pythonfiles/mchacks/save_images"
img="C:/pythonfiles/mchacks/save_images/img"
#tra=training("C:/pythonfiles/mchacks/gun_examples","C:/pythonfiles/mchacks/no_guns", size = [400,400])
tran=joblib.load("C:/pythonfiles/mchacks/saveddata.pkl")
#new_img = grayscaling("C:/pythonfiles/mchacks")
number=predict(tran,"C:/pythonfiles/mchacks")


if number==0 :
    for files in os.listdir(directory_path):
        if files.endswith("jpg") or files.endswith("png"):
            demo = open(directory_path, "rb")
            tiles=image_slicer.slice(demo,4) 
            image_slicer.save_tiles(tiles, there_images)
            #tr=training("C:/pythonfiles/mchacks/gun_examples","C:/pythonfiles/mchacks/no_guns")
            nb=predict(tran,"C:/pythonfiles/mchacks/save_images")
            if nb==0:
                for files in os.listdir(there_images):
                    if files.endswith("jpg") or files.endswith("png"):
                        dem = open(there_images, "rb")
                        tile=image_slicer.slice(dem,8) 
                        image_slicer.save_tiles(tile,img )
                        nbu=predict(tran,"C:/pythonfiles/mchacks/img")
                        if nbu==1:
                            print("YOu found a gun!")

else:
    print("Warning! A gun!")
            
        
"""" image_slicer.save_tiles( tiles,directory='D:\shoppin center _ Google Search\cropped')
        for dirname in os.listdir("."):
            if os.path.isdir(dirname):
                for i, filename in enumerate(os.listdir(dirname))
            os.rename(dirname + "/" + filename, dirname + "/" + str(i) + ".jpg")
                 
  
os.chdir('C:/Users/Renata/Desktop/')


im=Image.open('Crome.png')

# crete a loop that will 
imgwidth, imgheight= im.size
fHei= imgheight/2
fWid= imgheight/2

num=0

for i in range(0,imgwidth, int(fWid)):
    for j in range(0, imgheight, int(fHei)):
        area= (j,i,j+fHei, i+fWid)
        cropped=im.crop(area)
        cropped.save(str(num)+'.png')
        num=num+1
 """       