def main():
    print(upper(input(": ")))

def upper(input):
    result = ""
    
    for ch in input:

        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else: 
            result += ch
    return result 

main()