def main():
    swap(10,20)

def swap(a,b):
    temp = a
    a = b
    b = temp
    print(f"a:{a}, b:{b}")

main()