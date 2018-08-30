from math import sqrt
def distance(x1, x2, y1, y2, z1, z2):
	return sqrt(sqr(x1-x2) + sqr(y1-y2) + sqr(z1-z2))

def sqr(x):
	return pow(x, 2)
