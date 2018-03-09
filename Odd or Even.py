def getnum():
    num = int(input("Please enter your number : "))
    if num <= 0:
        print("Please enter only positive values")
        num = getnum()
    return num


def finding():
    try:
        nm = getnum()
    except ValueError:
        print("Please enter numbers only ")
        finding()
    else:
        if nm % 2 == 0:
            print("Given number is a even number..")
        else:
            print("Given number is Odd number...")

finding()
input()
