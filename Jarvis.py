import math

class Jarvis:
    def jarvisMarch(points):
        hull = []
        # get the leftmost point , initialize to cur
        left = points[0]
        for p in points:
            if p[0] < left[0]:
                left[0] = p[0]
        curPoint = left 
        curSlope = 1000000
        hull.append(left)
        hullFinished = False

        # while we haven't reached the original point again:
        while hullFinished == False:
            # choose the point that has the greatest angle w/ respect to the current point
            if len(points) <= 1:
                break
            bestPoint = points[1]
            minSlopeDifference = 100000
            for p in points:
                if curPoint[0] != p[0]:
                    pSlope = (curPoint[1] - p[1]) / (curPoint[0] - p[0])
                    if abs(curSlope - pSlope) < minSlopeDifference:
                        minSlopeDifference = abs(curSlope - pSlope)
                        bestPoint = p
                
            #remove bestPoint from points
            points.remove(bestPoint)

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

