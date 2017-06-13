# Uses python3
import sys,datetime
startTime=datetime.datetime.now()

def lcm(a, b):
	# prod=a*b
	# prodL=length(prod)
	# numL=0
	# if a > b:
	# 	numL=length(a)
	# else:
	# 	numL=length(b)
	i=0
	while i<a*b:
		if a>b:
			if (a*i)%b==0:
				return i

		else if b>a:
			if ((b*i)%a==0):
				return i
		i++



	

# def length(num):
# 	count =1
# 	while(num/10!=0):
# 		num=num/10
# 		count++
# 	return count

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
    print datetime.datetime.now()-startTime

