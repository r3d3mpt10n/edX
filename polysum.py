import math

def polysum(n,s):
    perim = n*s
    area = ((0.25*n*s**2)/math.tan(math.pi/n))
    sum = round(((perim**2) + area),4)
    return(sum)

def main():
    n = 80
    s = 70
    print(polysum(n,s))

main()