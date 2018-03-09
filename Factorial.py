def getnumber():
    num = int(input("Please enter your number to find factorial : "))
    if num <= 0:
        print("please enter number greater than Zero ")
        num = getnumber()
    return num
def finding():
    re = 1
    try:
        nm = getnumber()
    except ValueError:
        print("Please enter number's only ")
        finding()
    else:
        for i in range(1, nm+1):
            re = re * i
        print("Factorial of a given number is : ", re)
finding()
input()
