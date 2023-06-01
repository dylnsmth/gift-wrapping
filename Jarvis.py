
class Jarvis:
    def jarvisMarch(points):

        # start with the leftmost point , initialize to cur
        l = points[0]
        for p in points:
            if p[0] < l:
                l = p
        cur = l 
        hullFinished = False

        # while we haven't reached the original point again:
        while hullFinished == False:
            # choose the point that has the greatest angle w/ respect to the current point
            
            # update cur
    # return the hull

    def getAngle(point1, point2):
        #get the angle between these two points



def main():
    p1 = (2,3)
    p2 = (1, 3)
    p3 = (3,4)
    p4 = (5,3)
    p5 = (0,1)
    points = set(p1, p2, p3, p4, p5)
    Jarvis.jarvisMarch(points)


if __name__ == "__main__":
    main()

