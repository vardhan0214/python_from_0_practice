def main():
    print(reverse("abcdef"))

def reverse(ip):
    rev = ""
    for i in range(len(ip)):
        rev += ip[len(ip)-i-1]

    return rev

main()