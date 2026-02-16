def main():
    swap_without_third(10,200)

def swap_without_third(a,b):
    a = a^b
    b = a^b
    a = a^b

    print(f"a:{a}, b:{b}")

main()