import math

def main():
    print(valid_triangle(int(input(": ")),int(input(": ")),int(input(": "))))

def valid_triangle(a,b,c):
    return abs(a-b)< c <a+b and abs(a-c)< b <a+c and abs(b-c)< a <b+c

main()