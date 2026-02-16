def main():
    print(lexicographical_comparison(input(": ").lower(),input(": ").lower()))

def lexicographical_comparison(name1, name2):
    if name1 < name2:
        return f"{name1} comes before {name2}"
    elif name1 > name2:
        return f"{name2} comes before {name1}"
    else:
        return f"Both names are lexicographically equal"

main()