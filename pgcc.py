# This program calculates the smallest common multiplier of two numbers a and b
#first, lets create an algorith to calculate greatest common
import sys

# imperative style
def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a%b)

# functional style
def GCDfun(a, b):
    while b:
        a, b = b, a % b
    return a

# you can calculate the Greatest Common multiplier of a and b by multiplying
# them and the divide by their GCD
def GCM(a, b):
    return ((a * b)//GCD(a, b))

print(int(GCM(int(sys.argv[1], 10), int(sys.argv[2], 10))))
