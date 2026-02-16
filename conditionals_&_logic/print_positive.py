def main():
    list = [10,-5,90,-22,12,20]
    print_pos(list)

def print_pos(list):
    for i in list:
        if i>0:
            print(i,end=" ")

main()