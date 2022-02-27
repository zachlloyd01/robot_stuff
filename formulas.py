import math
from point2d import Point2D as p2d

def get_circle_intersections(x0=0, y0=0, r0=0, x1=0, y1=0, r1=0):
    '''
        x0, y0, r0 = circle1\n
        x1, y1, r1 = circle2.

        Finds all intersection points
    '''
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        #x-coord of circle intersection
        a=(r0**2-r1**2+d**2)/(2*d)
        #y-coord of circle intersection
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d

        return [
            p2d(x3, y3),
            p2d(x4, y4)
        ]

def get_distance(pos1: p2d, pos2: p2d):
    return math.sqrt((pos2.x - pos1.x)**2 + (pos2.y - pos1.y)**2)
print(get_circle_intersections(0,0,5,3,0,7))