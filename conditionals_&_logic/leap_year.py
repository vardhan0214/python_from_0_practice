def main():
    leap_year(1600)

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Yes it's a Leap Year!")
            else:
                print("No it's not a Leap Year")
        else:
            print("Yes it's a Leap Year!")
    else:
        print("No it's not a Leap Year") 

main()