def main():
    float_sep(440.203445)

def float_sep(f):
    s = str(f)
    i , d = s.split('.')
    print(f"Integer: {i} + Decimal: {d}")

main()
