# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	points = [] 
	#write your code here
	setList = []
	some = []

	for s in segments:
		list1=[i for i in range(s.start,s.end + 1)]
		setList.append(set(list1))

   	#I have now a list of sets containing all possible combination
   	#Complexity till now is n*n.Lets complete this first.

	#Find if there is an element that satisfies all conditions.
	for i in range(len(setList)):
		#compare as much sets as possible to find a comman point
		for j in range(i+1 , len(setList)):
			if(not setList[i].isdisjoint(setList[j])):
				sim = setList[i].intersection(setList[j])
				some.append(sim)
	print(some)
			

	

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    # print(len(points))
    # for p in points:
    #     print(p, end=' ')
