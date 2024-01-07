import math

def dist ( x1,y1,x2,y2):
    dist_x1 = abs(x1-x2)
    dist_x2 = abs(y1-y2)

    distance = math.sqrt((dist_x1*dist_x1) + (dist_x2*dist_x2))
    print("IN DIST : ",dir())
    return distance


def cirumference(x1,y1,x2,y2):
   
    r = dist(x1,y1,x2,y2)
    print("IN CIRCUM : ",dir())
    return (2*(22/7)*r)


print(f"{cirumference(0,0,4,4):0,.2f}")















def dist(x1,x2,y1,y2):
        dist_x1=abs(x1-x2)
        dist_x2=abs(y1-y2)

        distance = math.sqrt((dist_x1*dist_x1)+(dist_x2 * dist_x2))
        print("print in dist:",dir())
        return distance

def circumference(x1,x2,y1,y2):
     r=dist(x1,y1,x2,y2)
     print("IN CIRCUM : ",dir())
     return (2*(22/7)*r)

print(f"{circumference(0,0,4,4):0,.2f}")
def dist(x1,x2,y1,y2):
        dist_x1=abs(x1-x2)
        dist_x2=abs(y1-y2)

