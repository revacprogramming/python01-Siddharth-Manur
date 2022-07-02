# Functions


def computepay(h, r):
	if(h>40):
		p = 1.5*r*(h-40)+(40*r)
	else:
		p = h*r
	return p

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hrs,rate)
print("Pay: ", p)
