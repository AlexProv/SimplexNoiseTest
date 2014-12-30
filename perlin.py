import random
def Noise(x,y,octave):
    primes = getPrimes(octave)
    n = x*primes[0] + y*primes[1]
    n = (n<<primes[2]) ^ n
    random.seed(n)
    return random.random()

def getPrimes(x):
    primesList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109] 
    random.seed(x)
    return [ primesList[i] for i in sorted(random.sample(xrange(len(primesList)), 3)) ] 

import math
def Cosine_Interpolate(a, b, x):
    ft = x * math.pi
    f = (1 - math.cos(ft)) * .5
    return  a*(1-f) + b*f
 

Persistance = 0.25
NumberOfOctaves = 4
def PerlinNoise2D(x,y):
    total = 0
    p = Persistance
    n = NumberOfOctaves - 1

    for i in range(n):
        frequency = pow(2,i)
        amplitude = pow(p,i)

        total += InterpolateNoise(x * frequency, y * frequency,i) * amplitude
        
    return total


def InterpolateNoise(x,y,octave):
    ix = int(x)
    iy = int(y)

    fracX = x - ix
    fracY = y - iy 

    v1 = SmoothNoise(ix,iy,octave) 
    v2 = SmoothNoise(ix + 1, iy,octave)
    v3 = SmoothNoise(ix, iy + 1,octave)
    v4 = SmoothNoise(ix + 1, iy + 1,octave)

    i1 = Cosine_Interpolate(v1,v2,fracX)
    i2 = Cosine_Interpolate(v3,v4,fracX)

    return Cosine_Interpolate(i1,i2,fracY)

def SmoothNoise(x,y,octave):
    corners = ( Noise(x-1, y-1,octave)+Noise(x+1, y-1,octave)+Noise(x-1, y+1,octave)+Noise(x+1, y+1,octave) ) / 16
    sides   = ( Noise(x-1, y,octave)  +Noise(x+1, y,octave)  +Noise(x, y-1,octave)  +Noise(x, y+1,octave) ) /  8
    center  =  Noise(x, y,octave) / 4
    return corners + sides + center