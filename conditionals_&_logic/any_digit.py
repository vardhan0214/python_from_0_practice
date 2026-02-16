def main():
    print(any_digit(input(": ")))

def any_digit(ip):

    for i in range(len(ip)):
        try:
            if int(ip[i]):
                return True
        except:
            continue
    return False
    
main()

# if int("1") == 1:
#     print(True)