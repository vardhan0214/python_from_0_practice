def main():
    print(simple_cal(2,"+",5))

def simple_cal(a,op,b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b 
    
main()