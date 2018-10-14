import sys
import queue

def resturant(q):
"""Given a circle of restraunts, with the restaurants are numbered 0 through N−1 and, since the 
restaurants form a circle, you can only travel from restaurant to restaurant i+1.  Since it takes 
some amount of energy to get from one restaurant to the next, it’s possible that you could get stuck before 
completing the restaurant cycle!  You want to figure out at which restaurant to begin so that you can travel to all of them.
"""
	energy = 0
	dist = 0
	pos = 1
	while q.empty() == False:
		c = q.get()
		energy += c[0]
		dist += c[1]
		if energy < dist:
			q.put(c)
			energy -= c[0]
			dist -= c[1]
			pos += 1
	print(pos)

def driver():
	resturants = queue.Queue()
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			energy, dist = int(in_data[0]), int(in_data[1])
			resturants.put((energy, dist))
	resturant(resturants)

if __name__ == "__main__":
	driver()
