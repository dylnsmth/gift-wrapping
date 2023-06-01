import math

def angle_betwixt(p1, p2, p3):
    point1 = [p1[0], p1[1]]
    point2 = [p2[0], p2[1]]
    point3 = [p3[0], p3[1]]
    point1[0] -= point2[0]
    point1[1] -= point2[1]
    point3[0] -= point2[0]
    point3[1] -= point2[1]
#     # using dot product formula
    angle = math.acos((point1[0]*point3[0] + point1[1]*point3[1]) / (math.hypot(point1[0], point1[1]) * math.hypot(point3[0], point3[1])))
    return angle

def orientation(point1, point2, point3):
    value = (point2[1] - point1[1])*(point3[0]-point2[0]) - (point2[0]-point1[0])*(point3[1]- point2[1])
    return value

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
        
        point1 = [left[0], -1000000]
        point2 = left
        hull.append(left)
        hullFinished = False

        # while we haven't reached the original point again:
        while hullFinished == False:
            bestPoint = p[0]
            bestAngle = -math.inf

            if len(points) == 0:
                break
            bestPoint = points[0]
            
            # choose the point that has the greatest angle w/ respect to the current point
            for p in points:
                if (p == point1) or (p == point2):
                    continue
                angle = angle_betwixt(point1, point2, p)
                if angle > bestAngle:
                    bestAngle = angle
                    bestPoint = p

            #remove bestPoint from points
            points.remove(bestPoint)

            hull.append(bestPoint)
            point1 = point2
            point2 = bestPoint

            # if we get back to the start, we're done :)
            if bestPoint == left:
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

