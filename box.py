#!/usr/bin/python
def box(com): # com is list, xyz is int
	x = 1
	y = 1
	z = com[2]
	xs = []
	ys = []
	zs = []
	points = []
	p1 = [com[0]+x, com[1], com[2]+15]
	points.append(p1)
	p2 = [com[0]-x, com[1], com[2]+15]
	points.append(p2)
	p3 = [com[0], com[1]+y, com[2]+15]
	points.append(p3)
	p4 = [com[0], com[1]-y, com[2]+15]
	points.append(p4)
	p5 = [com[0]+x, com[1], com[2]-15]
	points.append(p5)
	p6 = [com[0]-x, com[1], com[2]-15]
	points.append(p6)
	p7 = [com[0], com[1]+y, com[2]-15]
	points.append(p7)
	p8 = [com[0], com[1]-y, com[2]-15]
	points.append(p8)
	for point in points:
		xs.append(point[0])
		ys.append(point[1])
		zs.append(point[2])
	return xs,ys,zs	
	
