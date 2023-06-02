import math

# Returns the point with least y coordinate from a list of 2D points. Tiebreaker is least x.
def get_minimum_y(points):
	minimum_point = [math.inf, math.inf]
	for point in points:
		if point[1] < minimum_point[1] or (point[1] == minimum_point[1] and point[0] < minimum_point[0]):
			minimum_point = point
	return minimum_point

# Transforms a list of 2D points into polar coordinates.
# Takes points from [x,y] -> [r,theta]
def get_polar_points(points):
	polar_points = []
	for point in points:
		r = math.sqrt(point[0]**2 + point[1]**2)
		if point[0] == 0:	# Don't divide by zero.
			theta = 0
		else:
			theta = math.atan(1.0 * point[1] / point[0])
			if theta < 0:
				theta = theta + math.pi
		new_point = [r, theta]
		polar_points.append(new_point)
	return polar_points

# Tacks on polar coordinates to the end of a list of points of form [x,y]
# Takes points from [x,y] -> [x,y,r,theta]
def extend_into_polar(points):
	polar_points = get_polar_points(points)
	for i, point in enumerate(points):
		points[i] = point + polar_points[i]
	return points

# Removes polar points from the end of a list of points of form [x,y,r,theta]
# Takes points from [x,y,r,theta] -> [x,y]
def restrict_from_polar(points):
	new_points = []
	for i, point in enumerate(points):
		new_points.append([point[0], point[1]])
	return new_points

# Translates points with respect to a new origin point.
def recenter_points(points, center):
	for point in points:
		point[0] -= center[0]
		point[1] -= center[1]
	return points

# Reverse translates points with respect to original origin point.
# Undoes recenter_points when used with same center point
def uncenter_points(points, center):
	for point in points:
		point[0] += center[0]
		point[1] += center[1]
	return points

def prune_points(points):
	i = 0
	while i < len(points)-1:
		while points[i][3] == points[i+1][3]:
			points.remove(points[i])
		i = i+1
	return points

# Calculates orientation of three odered points. Returns:
	# 0 if colinear
	# positive value if point1 -> point2 -> point3 -> point1 goes clockwise
	# negative value if point1 -> point2 -> point3 -> point1 goes counter-clockwise
def orientation(point1, point2, point3):
	value = (point2[1] - point1[1])*(point3[0]-point2[0]) - (point2[0]-point1[0])*(point3[1]- point2[1])
	return value

# Performs the Graham Scan on a list of 2D of points; returns the convex hull as an ordered list.
def graham_scan(points):
	min_point = get_minimum_y(points)
	points.remove(min_point)
	# Sorts all points by counter-clockwise angle from min_point. 
	# Shift points with respect to min_point, find angles and lengths, sort them, prune any duplicate angles, then hide angles/lengths and undo shift.
	points = recenter_points(points, min_point)
	points = extend_into_polar(points)
	points = sorted(points, key=lambda element: (element[3], element[2]))
	points = prune_points(points)
	points = restrict_from_polar(points)
	points = uncenter_points(points, min_point)
	# Make a stack to keep track of our convex hull. 
	stack = [min_point, points[0], points[1]]
	# For all points remaining, add it to the stack after removing all points previously defining the hull that are unnecessary.
	for i in range(2, len(points)):
		stack_end = len(stack)-1
		# If the orientation of the last two points added to the hull and the next point is non-negative, the last added point is unnecessary.
		while orientation(stack[stack_end-1], stack[stack_end], points[i]) >= 0:
			stack.remove(stack[stack_end])
			stack_end = len(stack)-1
		stack.append(points[i])
	return stack

def main():
    points1 = [[2,3], [1, 2], [1.4,5], [3, 2.1], [4,3], [5, 1.3], [2, 4]]
    points2 = [[1,3], [5,6], [2,4], [6,8], [1,6], [2,5], [5,2], [3,3], [1,7], [9,2], [2,2]]
    
    points = eval(input("please enter a list of points here:\n"))
    print("\nThe points in the convex hull are:")
    print(graham_scan(points))


main()
