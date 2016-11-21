import math

def fractal_box_count(pointlist, scale):
        """Returns the box coverage of pointlist for boxes of size 
scale,"""

        boxlevel = 1.0 / scale
        pointdict = {}

        for point in pointlist:
                box = (int(point[0] * boxlevel),
                        int(point[1] * boxlevel),
                        int(point[2] * boxlevel))
                if not pointdict.has_key(box):
                        pointdict[box] = 1

        return len(pointdict)

        return (math.log(num), math.log(boxlevel))

def fractaldim(pointlist, scale1, scale2):
        """Returns the approximate fractal dimension of pointlist
between box scales scale1 and scale2."""

        log = math.log
        c1 = fractal_box_count(pointlist, scale1)
        c2 = fractal_box_count(pointlist, scale2)
        return (log(c2) - log(c1)) / (log(1.0/scale2) - log(1.0/scale1))

print "line dimension"
list1d = []
for x in xrange(100):
    list1d.append((x/100.0, 0, 0))

for level in xrange(1,10):
    scale1 = (.5 ** level)
    scale2 = scale1 / 4.0
    print level, fractaldim(list1d, scale1, scale2)

print "plane dimension"
list2d = []
for x in xrange(100):
   for y in xrange(100):
       list2d.append((x/50.0, y/50.0, 0))

for level in xrange(1,10):
    scale1 = (.5 ** level)
    scale2 = scale1 / 4.0
    print level, fractaldim(list2d, scale1, scale2)

print "space dimension"
list3d = []
for x in xrange(30):
   for y in xrange(30):
      for z in xrange(30):
          list3d.append((x/120.0, y/120.0, z/120.0))

for level in xrange(1,10):
    scale1 = (.5 ** level)
    scale2 = scale1 / 4.0
    print level, fractaldim(list3d, scale1, scale2)

def makekoch(x1, y1, x2, y2, level, flist=[]):
    xd = (x2 - x1)
    yd = (y2 - y1)
    xa = x1 + xd / 3.0
    ya = y1 + yd / 3.0
    xb = x1 + xd * 2.0 / 3.0
    yb = y1 + yd * 2.0 / 3.0
    xm = (x1 + x2) / 2.0 - 0.866 * yd / 3.0
    ym = (y1 + y2) / 2.0 + 0.866 * xd / 3.0
    flist.append((xa,ya,0))
    flist.append((xm,ym,0))
    flist.append((xb,yb,0))
    if (level > 0):
       makekoch(x1, y1, xa, ya, level-1, flist)
       makekoch(xa, ya, xm, ym, level-1, flist)
       makekoch(xm, ym, xb, yb, level-1, flist)
       makekoch(xb, yb, x2, y2, level-1, flist)
    return flist

print "koch dimension"
listfract = makekoch(0,0,1,0,6)
for level in xrange(1,10):
    scale1 = (.5 ** level)
    scale2 = scale1 / 4.0
    print level, fractaldim(listfract, scale1, scale2)

