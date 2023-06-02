import math

def jarvisMarch(points):
    hull = []

    # get the leftmost point
    left = getLeftmostPoint(points)

    # hull starts with leftmost point and temporary second point to form axis
    hull.append([left[0], left[1] - 1]) # arbitary point with y less than leftmost point; forms a vertical axis 
    hull.append(left)

    hullFinished = False

    # while we haven't reached the original point again:
    while not hullFinished:
        bestPoint = points[0]
        bestAngle = -math.inf
        bestDistance = -math.inf

        # choose the point that has the greatest angle w/ respect to the current point
        for p in points:
            # doesn't consider the two previous points which form the angle
            if (p in hull[-2:]):
                continue

            angle = angleBetween(hull[-2], hull[-1], p)
            distance = math.dist(hull[-1], p)

            # if this angle is larger than the previous best, choose it
            # in a tie, consider the furthest away point
            if angle > bestAngle or (angle == bestAngle and distance > bestDistance):
                bestPoint = p
                bestAngle = angle
                bestDistance = distance # for tiebreakers

        # handling the point with the greateset angle
        if bestPoint == left:
            # if we get back to the start, we're done :)
            hullFinished = True
        else:
            # remove bestPoint from points and add it to the hull
            points.remove(bestPoint)
            hull.append(bestPoint)


    # removes temporary point from hull
    hull.pop(0)
    # return the hull
    return hull

# finds the leftmost point in a list
def getLeftmostPoint(points):
    left = points[0]
    for p in points:
        if p[0] < left[0]:
            left = p
    return left

# finds the angle between three points
def angleBetween(p1, p2, p3):
    # avoid overwriting the points
    point1 = p1.copy();
    point2 = p2.copy();
    point3 = p3.copy();
    # makes it so point2 is the origin
    point1[0] -= point2[0]
    point1[1] -= point2[1]
    point3[0] -= point2[0]
    point3[1] -= point2[1]
    # using dot product formula
    angle = math.acos((point1[0]*point3[0] + point1[1]*point3[1]) / (math.hypot(point1[0], point1[1]) * math.hypot(point3[0], point3[1])))
    return angle

def main():
    p1 = [2,3]
    p2 = [1, 2]
    p3 = [1.4,5]
    p4 = [3, 2.1]
    p5 = [4,3]
    p6 = [5, 1.3]
    p7 = [2, 4]
    points1 = [p1, p2, p3, p4, p5, p6, p7]
    points2 = [[1,3], [5,6], [2,4], [6,8], [1,6], [2,5], [5,2], [3,3], [1,7], [9,2], [2,2]]
    
    points = eval(input("please enter a list of points here:\n"))
    print("\nThe points in the convex hull are:")
    print(jarvisMarch(points))


main()