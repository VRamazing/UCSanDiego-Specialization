# Uses python3
import sys,datetime
# startTime=datetime.datetime.now()

def lcm(a, b):

	if a>=b:
		small=b
		large=a
	else:
		small=a
		large=b


	i=1
	while i<=a*b:
		#While loop Still goes to 10^16 for numbers 10^8 and 10^8
		if (large*i)%small==0:
				return large*i
				
		i+=1


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
    # print(datetime.datetime.now()-startTime)

