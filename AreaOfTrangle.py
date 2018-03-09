def getinput():
    try:
        side1 = float(input("Please enter your value for side 1 : "))
    except ValueError:
        print("Please enter Positive values and other than zero")
        getinput()
    else:
        return side1


def getinput2():
    try:
        side2 = float(input("Please enter your value for side 2 : "))
    except ValueError:
        print("Please enter Positive values and other than zero")
        getinput2()
    else:
        return side2


def getinput3():
    try:
       side3 = float(input("Please enter your value for side 3 : "))
    except ValueError:
        print("Please enter Positive values and other than zero")
        getinput3()
    else:
        return side3


def calarea():
    a = getinput()
    b = getinput2()
    c = getinput3()
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5


def main():
    print(calarea())


if __name__ == "__main__":
    main()
    input()
