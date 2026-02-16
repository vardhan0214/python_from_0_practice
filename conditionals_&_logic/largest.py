def main():
    largest(101,219,100)

def largest(a,b,c):
    if (a>b):
        if (a>c):
            print(f"{a} is largest")
        else:
            print(f"{c} is largest")
    else:
        if (b>c):
            print(f"{b} is largest")
        else:
            print(f"{c} is largest")

main()