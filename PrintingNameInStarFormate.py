def getname():
    name = input("Please enter your name : ")
    return name


def printa():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (5 > column > 1)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printb():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 6) and (row != 0 and row != 6) and (row != 3)) or (
                    ((row == 0 or row == 6) or row == 3) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printc():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 7) and (row != 0 and row != 6)) or (
                    (row == 0 or row == 6) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printd():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 6) and (row != 0 and row != 6)) or (
                    (row == 0 or row == 6) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printe():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 1) or (
                    ((row == 0 or row == 6) or row == 3) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
    print(result_str)


def printf():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1) or ((row == 0 or row == 3) and (0 < column < 6)):
                result_str = result_str + "* "
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
    print(result_str)


def printg():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 0 or column == 5) and (column < 4 or row > 2) and (row != 0 and row != 6)) or (
                    (row == 6 or row == 0 or (column != 1 and row == 3)) and (0 < column < 6)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printh():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 0 or column == 6) or ((row == 3) and (0 < column < 6)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printi():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 3 and (row != 0 and row != 6)) or (
                    (row == 0 or row == 6) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printj():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6 or row == 5) and (
                    (2 <= column <= 3 or row != 6) and (column == 1 or row != 5)) and (0 < column < 7))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printk():
    result_str = ""
    i, p = 0, 4
    x, q = 4, 2
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 0) or (
                    (row == i and column == x) or (row == p and column == q) or (column == 3 and row == 5) or (
                    column == 4 and row == 6) and (0 < column < 5))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
        i += 1
        x -= 1
    print(result_str)


def printl():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 0) or ((row == 6) and (0 < column < 6)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printm():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 0 or column == 6) or (
                    (row == 1 and column == 1) or (row == 2 and column == 2) or (column == 3 and row == 3) or (
                    column == 4 and row == 2) or (column == 5 and row == 1) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printn():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((column == 0 or column == 6) or (
                    (row == 1 and column == 1) or (row == 2 and column == 2) or (column == 3 and row == 3) or (
                    column == 4 and row == 4) or (column == 5 and row == 5) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printo():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 6) and (row != 0 and row != 6)) or (
                    (row == 0 or row == 6) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printp():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 5) and (column < 4 or row < 4)) or (
                    (row == 3 or row == 0) and (0 < column < 5))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printq():
    for row in range(8):
        for col in range(12):
            if ((col == 0 or col == 4) and (0 < row < 6)) or (
                    (row == 0 or row == 6) and (0 < col < 4)) or (
                    (row == 5 and col == 1) or (row == 7 and col == 3)):
                print("* ", end="")
            else:
                print(end="  ")

        print()


def printr():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or (column == 6 and row < 4) or (column == 3 and row == 4) or (
                    column == 4 and row == 5) or (column == 5 and row == 6)) and (row != 0 and row != 3)) or (
                    (row == 0 or row == 3) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def prints():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((((column == 0 and row < 4) or (column == 6 and row > 3)) and (row != 0 and row != 6) and (
                    row != 3)) or (((row == 0 or row == 6) or (row == 3)) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printt():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 3 and (row != 0 and row != 6)) or (row == 0 and (0 < column < 6)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printu():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 6) and (row != 0 and row != 6)) or (
                    (row == 6) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def printv():
    result_str = ""
    i, x, y = 0, 0, 12
    for row in range(0, 7):
        for column in range(0, 14):
            if ((row == i and column == x) or (column == y and (6 > row == i))) and (0 <= column < 15):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
        i += 1
        x += 1
        y -= 1
    print(result_str)


def printw():
    result_str = ""
    i, x, y = 0, 0, 12
    a, b = 12, 24
    for row in range(0, 7):
        for column in range(0, 28):
            if ((((row == i and column == x) or (column == y and (6 > row == i)) or (
                    row == i and column == a) or (column == b and (6 > row == i))) and (0 <= column < 29))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
        i += 1
        x += 1
        y -= 1
        a += 1
        b -= 1
    print(result_str)


def printx():
    result_str = ""
    i, x, y = 0, 0, 6
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == i and column == x) or (column == y and (row == i))) and (0 <= column < 7):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
        i += 1
        x += 1
        y -= 1
    print(result_str)


def printy():
    result_str = ""
    i, x, y = 0, 0, 6
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == i and (4 > column == x)) or (column == y and (row == i))) and (0 <= column < 7):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
        i += 1
        x += 1
        y -= 1
    print(result_str)


def printz():
    result_str = ""
    a, b = 6, 0
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == 0 or row == 6) or (column == a and row == b)) and (0 <= column <= 6):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
        a -= 1
        b += 1
    print(result_str)


def printname():
    n = getname()
    for i in range(len(n)):
        if n[i] == "A":
            printa()
        elif n[i] == "B":
            printb()
        elif n[i] == "C":
            printc()
        elif n[i] == "D":
            printd()
        elif n[i] == "E":
            printe()
        elif n[i] == "F":
            printf()
        elif n[i] == "G":
            printg()
        elif n[i] == "H":
            printh()
        elif n[i] == "I":
            printi()
        elif n[i] == "J":
            printj()
        elif n[i] == "K":
            printk()
        elif n[i] == "L":
            printl()
        elif n[i] == "M":
            printm()
        elif n[i] == "N":
            printn()
        elif n[i] == "O":
            printo()
        elif n[i] == "P":
            printp()
        elif n[i] == "Q":
            printq()
        elif n[i] == "R":
            printr()
        elif n[i] == "S":
            prints()
        elif n[i] == "T":
            printt()
        elif n[i] == "U":
            printu()
        elif n[i] == "V":
            printv()
        elif n[i] == "W":
            printw()
        elif n[i] == "X":
            printx()
        elif n[i] == "Y":
            printy()
        elif n[i] == "Z":
            printz()


def main():
    printname()
    input()


if __name__ == "__main__":
    main()
