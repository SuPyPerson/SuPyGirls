
"""
fractaldim2.py - calculate fractal dimensions
Adopted by Huaiyu Zhu from

From: spe...@?.com (Jake Speed)
Newsgroups: comp.lang.python
Subject: Re: Fractal Dimension Computation in Python Code
Date: Fri, 29 Sep 2000 20:01:10 -0000
"""

from math import log
from numpy import *
from random import randrange
from csv import reader

def cvsread(afile):
    with open(afile, 'rb') as csvfile:
        spamreader = reader(csvfile, delimiter=',', quotechar='"')
        y = [a for a in spamreader]
        yy = zip(*y)
        k = yy[-3][2:]
        kk = [float(a.replace(',','.')) for a in k]
        return kk


def N(points, scale):
    """Return (num of coverage, scale) of points by boxes of size 1/scale"""
    unique = {}
    for point in points:
        try:
            box =  tuple((point * scale).astype(int))
        except:
            box = tuple([int(point * scale)])
        unique[box] = 1
    return float(len(unique)), scale

def dim(points):
    """ Calculate dimensions of points at various scale = 2**level"""
    f0 = 1, 1
    #print(points)
    for level in xrange(1, 12):
        f1 = N(points, 2.0**level)
        dim = log(f1[0]/f0[0]) / log(f1[1]/f0[1])
        print ("%2d:  %.4g" % (level, dim))
        f0 = f1

M = array([[0,-1], [1,0]]) * sqrt(3)/2

def makekoch(x1, x2, level, flist=[]):
    """ Return a list of points on Koch curve, subdivided levels """
    if level == 0: return flist
    xd = (x2 - x1) / 3.
    xa = x1 + xd
    xb = x2 - xd
    xm = (x1 + x2) / 2.0 - M.dot( xd)
    flist.append(xa)
    makekoch(x1, xa, level-1, flist)
    makekoch(xa, xm, level-1, flist)
    flist.append(xm)
    makekoch(xm, xb, level-1, flist)
    makekoch(xb, x2, level-1, flist)
    flist.append(xb)
    return flist

#------------------------------------------------------------------
if __name__ == "__main__":
    print ("line dimension")
    x = array(arange(100)/100.)#[:,NewAxis]
    dim(x)
    
    print ("random dimension")
    x = array(arange(100)*randrange(100)/100.)#[:,NewAxis]
    dim(x)

    print ("plane dimension")
    list2d = []
    for x in xrange(100):
        for y in xrange(100):
            list2d.append(array((x, y))/100.0)
    dim(list2d)

    print ("space dimension")
    list3d = []
    for x in xrange(30):
        for y in xrange(30):
            for z in xrange(30):
                list3d.append(array((x, y, z))/30.0)
    dim(list3d)

    print ("koch dimension")
    listkoch = makekoch(array((0,0)), array((1,0)), 7)
    dim(listkoch)
    y = [0.25, 1.27, 0.47, 0.45, 0.7, 0.83, 0.65, 7.45, 2.5, 1.98, 2.22, 2.98,
         2.13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.92, 0.82, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 7.5, 11.12, 1.23, 5.02, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.17, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    #print ("aluno9 dimension")
    for i in range(1,10):
        print('aluno %d dimension'%i)
        aluno = cvsread('aluno%d.csv'%i)
        dim(aluno)
    #dim(y)
    
