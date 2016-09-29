import sys
from os import listdir
import os
from os.path import isfile, join
import glob
import shutil
from images2gif import writeGif
from PIL import Image
import os

GlobCSV = glob.glob("./*.csv")
GlobPNG = glob.glob("./*.csv")
myList = sorted(set(GlobCSV+GlobPNG))
ListFiles = []

for image in GlobCSV:
	tmp = image.split("/")[1]
	tmpImage = tmp.split("-")[0]+"-"+tmp.split("-")[1]
	ListFiles.append(tmpImage)
	if not os.path.exists(tmpImage):
	    os.mkdir(tmpImage)

ListFiles = sorted(set(ListFiles))

print ListFiles

files = os.listdir("./")

for eachImage in ListFiles:
	for f in files:
	    if (f.startswith(eachImage) and (	f != eachImage)):
		shutil.move(os.path.join("./", f), os.path.join(eachImage, f))
		print "./"+f

files = os.listdir("./")
dossiers = []
for fileOne in files:
    if(("2016" in fileOne) and ("gif" not in fileOne) ):
	dossiers.append(fileOne)
print dossiers

TableauImages = "|Image|Description|Download|\n"
TableauImages += "|--|--|--|\n"
for eachImage in dossiers:
	file_names = sorted((fn for fn in os.listdir(eachImage) if fn.endswith('SC.png')))
	images = [Image.open("./"+eachImage+"/"+fn) for fn in file_names]
	# Correction needed: http://stackoverflow.com/questions/19149643/error-in-images2gif-py-with-globalpalette
	filename = "./"+eachImage+".gif"
	writeGif(filename, images, duration=0.05)
	TableauImages += "|<img src='https://github.com/kelu124/echomods/blob/master/croaker/data/examples/"+eachImage+".gif'>|Description|Download|\n"



f = open("./Intro.md", 'r')
intro_files = f.read()
f.close()

f = open("Readme.md","w+")
f.write(intro_files+"\n\n"+TableauImages)
f.close()



