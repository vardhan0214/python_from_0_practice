import math
def main():
    i = int(input(": "))
    # print(type(i))
    print(is_prime(i))

def is_prime(ip):
    # edge case 
    if ip == 1:
        return "False"
    i = 2
    # print(int(math.sqrt(ip)))
    while i<=int(math.sqrt(ip)):
        if ip%i == 0:
            return False
        i+=1
        # print(i)
    return True

main()