import simplex2D as sp 
import sys
import math
from PIL import Image, ImageDraw

def badway():
    #path = sys.argv[0]
    #name = sys.argv[1]
    #size = int(sys.argv[2])
    size = 10
    size = int(sys.argv[1])
    zoom = 0.005
    img = Image.new('RGBA',(size,size))
    #draw = ImageDraw.Draw(img)
    pixel = img.load()
    rgb = {}
    for i in range(size):
        for j in range(size):
            Rvalue = int(sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=0,hiBound=255,x=i*zoom,y=j*zoom))
            Gvalue = int(sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=0,hiBound=255,x=i*zoom*size,y=j*zoom*size))
            Bvalue = int(sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=0,hiBound=255,x=i*zoom*size*2,y=j*zoom*size*2))
            
            #pixel[i,j] = (value,value,value,255)
            rgb[(i,j)] = {'r':Rvalue,'g':Gvalue,'b':Bvalue}

    for (i,j),value in rgb.iteritems():

        pixel[i,j] = (value['r'],value['g'],value['b'],255)

    print 'done'
    img.show()

def main():
    size = int(sys.argv[1])
    seed = float(sys.argv[2])
    
    zoom = 0.005
    imgR = Image.new('RGBA',(size,size))
    imgG = Image.new('RGBA',(size,size))
    imgB = Image.new('RGBA',(size,size))
    #draw = ImageDraw.Draw(img)
    imgR = fillBNW(imgR,0,255,zoom,size,seed)
    #imgR = fillBNW(imgR,0,255,zoom,size)
    #imgG = fillBNW(imgG,500,255+500,zoom,size)
    #imgB = fillBNW(imgB,800,255+800,zoom,size)

    #img = filterToRGB(imgR,imgG,imgB,size)

    print 'done'
    imgR.show()
    #imgR.show()
    #imgG.show()
    #imgB.show()

def fillBNW(img,min,max,zoom,size,seed):
    
    pixel = img.load()
    
    for i in range(size):
        for j in range(size):
            value = int(sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=min,hiBound=max,x=i*zoom,y=j*zoom,seed = seed))
            pixel[i,j] = (value%255,value%255,value%255,255)

    return img

def filterToRGB(r,g,b,size):
    img = Image.new('RGBA',(size,size))
    pixel = img.load()
    Rpixel = r.load()
    Gpixel = g.load()
    Bpixel = b.load()

    for i in range(size):
        for j in range(size):
            rc = Rpixel[i,j][0]
            gc = Gpixel[i,j][1]
            bc = Bpixel[i,j][2]
            pixel[i,j] = (rc,gc,bc,255)
    return img

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

if __name__ == '__main__':
    main()


"""    for i in range(size):
        for j in range(size):
            value = int(sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=0,hiBound=16777214,x=i*zoom,y=j*zoom))
            value = hex(value)
            value = value[2:]
            pixel[i,j] = hex_to_rgb('#'+ str(value))
            
            #pixel[i,j] = (value,value,value,255)"""
            

