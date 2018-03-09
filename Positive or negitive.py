def getnum():
    num = float(input("Please enter your number : "))
    return num


def finding():
    try:
        nm = getnum()
    except ValueError:
        print("Please enter only number's not strings ")
        nm = finding()
    else:
        if nm >= 0 :
            print("Given number is positive")
        else:
            print("Given number is negitive")


finding()
input()
