def main():
    grade(69)

def grade(ip):
    if ip>=90:
        print("A")
    elif ip>=80:
        print("B")
    elif ip>=70:
        print("C")
    elif ip>=60:
        print("D")
    elif ip>=50:
        print("E")
    else:
        print("F")

main()