import math

points = [[1,3], [5,6], [2,4], [6,8], [1,6], [2,5], [5,2], [3,3], [1,7], [9,2], [2,2]]

def get_minimum_y(points):
	minimum_point = [math.inf, math.inf]
	for point in points:
		if point[1] < minimum_point[1]:
			minimum_point = point
		elif point[1] == minimum_point[1] and point[0] < minimum_point[0]:
			minimum_point = point
	return minimum_point

def get_polar_points(points):
	polar_points = []
	for point in points:
		r = math.sqrt(point[0]**2 + point[1]**2)
		if point[0] == 0:
			theta = 0
		else:
			theta = math.atan(1.0 * point[1] / point[0])
		new_point = [r, theta]
		polar_points.append(new_point)
	return polar_points
	
def extend_into_polar(points):
	polar_points = get_polar_points(points)
	for i, point in enumerate(points):
		points[i] = point + polar_points[i]
	return points

def constrict_from_polar(points):
	new_points = []
	for i, point in enumerate(points):
		new_points.append([point[0], point[1]])
	return new_points

def recenter_points(points, center):
	for point in points:
		point[0] -= center[0]
		point[1] -= center[1]
	return points

def uncenter_points(points, center):
	for point in points:
		point[0] += center[0]
		point[1] += center[1]
	return points

def orientation(point1, point2, point3):
	value = (point2[1] - point1[1])*(point3[0]-point2[0]) - (point2[0]-point1[0])*(point3[1]- point2[1])
	return value
		

# def angle_betwixt(point1, point2, point3):
#	print(point1)
#	print(point2)
#	print(point3)
#	point1[0] -= point2[0]
#	point1[1] -= point2[1]
#	point3[0] -= point2[0]
#	point3[1] -= point2[1]
#	# using dot product formula
#	angle = math.acos((point1[0]*point3[0] + point1[1]*point3[1]) / (math.hypot(point1[0], point1[1]) * math.hypot(point3[0], point3[1])))
#	print(angle)


def graham_scan(points):
	min_point = get_minimum_y(points)
	points.remove(min_point)
	points = recenter_points(points, min_point)
	points = extend_into_polar(points)
	points = sorted(points, key=lambda element: (element[3], element[2]))
	points = constrict_from_polar(points)
	points = uncenter_points(points, min_point)

	stack = [min_point, points[0], points[1]]
	for i in range(2, len(points)):
		stack_end = len(stack)-1
		while orientation(stack[stack_end-1], stack[stack_end], points[i]) >= 0:
			stack.remove(stack[stack_end])
			stack_end = len(stack)-1
		stack.append(points[i])


	return stack