def main():
    print(count_vowels("Hi! How are you?"))

def count_vowels(input):
    counter = 0
    for i in range(len(input)):
        if input[i] in ["a","e","i","o","u"]:
            counter += 1 

    return counter

main()