def main():
    print(is_palindrome("racecar"))

def is_palindrome(input):
    for i in range(len(input)):
        if (input[i]!=input[len(input)-i-1]):
            return False
    return True

main()