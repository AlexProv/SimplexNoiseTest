import simplex2D as sp 
import simplex
import sys
import math
from PIL import Image, ImageDraw

def __main__():
    #path = sys.argv[0]
    #name = sys.argv[1]
    #size = int(sys.argv[2])
    size = 10
    size = int(sys.argv[1])
    zoom = 0.0033
    img = Image.new('RGBA',(size,size))
    #draw = ImageDraw.Draw(img)
    pixel = img.load()

    for i in range(size):
        for j in range(size):
            value = sp.scaledOctaveNoise2D(octaves=10,persistence=0.25,scale=2.1,loBound=0,hiBound=255,x=i*zoom,y=j*zoom)
            value = int(value)
            pixel[i,j] = (value,value,value,255)

    img.show()


def marble_noise_2d(octaves, persistence, scale, x, y):
    """2D Marble Noise on the x-axis."""
    return math.cos(float(x) * scale + simplex.octave_noise_2d(
            octaves, persistence, float(scale) / 3.0, x, y)
        );

if __name__ == '__main__':
    __main__()


