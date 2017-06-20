# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    points = []
    final = []
    
    #write your code here

    for s in segments:
        points.append(s.start)
        points.append(s.end)

    points.sort()    
    dictPoints={}
    lenPoints=len(points)

    for i in range(points[0],points[lenPoints-1]+1):
        dictPoints[i] = 0
        for s in segments:
            if i >= s.start and i <= s.end:
                dictPoints[i] += 1
    
    list1=list(dictPoints.values())
    list1.sort(reverse = True)
    
    #Find the minimum num points that satisfies all lines.


    print(dictPoints)
    print(list1)
    return final

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
