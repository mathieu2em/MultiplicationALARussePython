import sys

initx = sys.argv[1]
inity = sys.argv[2]

x = int(initx, 10)
y = int(inity, 10)
sum = 0

def multRuss():
    global x
    global y
    global sum
    if x <= 1:
        print("the result of " + initx + " times "
              + inity + " is " + str(sum))
        return sum
    else:
        x = x>>1
        y = y<<1
        if (y%2==0) ^ (x%2==0)  : sum += y;
        return multRuss();

multRuss()
