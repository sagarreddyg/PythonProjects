def getinput1():
    try:
        num1 = int(input("Please enter your first number for swap: "))
    except ValueError:
        print("Please enter your number's only")
        num1 = getinput1()
    else:
        return num1
def getinput2():
    try:
        num2 = int(input("Please enter your second number for swap "))
    except ValueError:
        print("Please enter your number's only")
        num2 = getinput2()
    else:
        return num2
def main():
    a = getinput1()
    b = getinput2()
    c, d = b, a
    print("the Swaped out put is : {} to {} and {} to {}".format(a, c, b, d))
if __name__ == "__main__":
    main()
    input()
