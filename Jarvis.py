import math

class Jarvis:
    def jarvisMarch(points):
        hull = []
        # get the leftmost point , initialize to cur
        left = points[0]
        right = points[0]
        for p in points:
            if p[0] < left[0]:
                left = p
            if p[0] > right[0]:
                right = p

        curPoint = left 
        curSlope = math.inf
        hull.append(left)
        hullFinished = False
        rightReached = False

        # while we haven't reached the original point again:
        while hullFinished == False:
            if len(points) == 0:
                break
            bestPoint = points[0]
            minSlopeDifference = math.inf
            
            # choose the point that has the greatest angle w/ respect to the current point
            for p in points:
                if curPoint[0] != p[0]:
                    pSlope = (curPoint[1] - p[1]) / (curPoint[0] - p[0])
                    dif = abs(curSlope - pSlope) # calculate difference in slopes
                    print(dif)
                    # until we reach the rightmost point, we want the slope to be the closest one that is smaller than the current slope 
                    if (dif < minSlopeDifference or minSlopeDifference == math.inf) and not p == left and not rightReached and dif != 0:
                        minSlopeDifference = dif
                        bestPoint = p
                    elif (dif < minSlopeDifference or minSlopeDifference == math.inf) and rightReached:
                        minSlopeDifference = dif
                        bestPoint = p
                            
            #remove bestPoint from points
            points.remove(bestPoint)

            if bestPoint == right:
                rightReached = True

            hull.append(bestPoint)

            # update cur
            curPoint = bestPoint

            # if we get back to the start, we're done :)
            if curPoint == left:
                hullFinished = True
        # return the hull
        return hull


def main():
    p1 = [2,3]
    p2 = [1, 2]
    p3 = [1.4,5]
    p4 = [3, 2.1]
    p5 = [4,3]
    p6 = [5, 1.3]
    p7 = [2, 4]
    points = [p1, p2, p3, p4, p5, p6, p7]
    print(Jarvis.jarvisMarch(points))


if __name__ == "__main__":
    main()

