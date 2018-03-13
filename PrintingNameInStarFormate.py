def getname():
    name = input("Please enter your name : ")
    return name


def printname():
    n = getname()
    for i in range(len(n)):
        if n[i] == "A":
            result_str = ""
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (5 > column > 1)):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "B":
            result_str = ""
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 1 or column == 6) and (row != 0 and row != 6) and (row != 3)) or (
                            ((row == 0 or row == 6) or row == 3) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "C":
            result_str = ""
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 7) and (row != 0 and row != 6)) or (
                            (row == 0 or row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "D":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 1 or column == 6) and (row != 0 and row != 6)) or (
                            (row == 0 or row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "E":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 1 or column == 1)) or (
                            ((row == 0 or row == 6) or row == 3) and (column > 1 and column < 5))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + " "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "F":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 1 or column == 1)) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
                        result_str = result_str + "*"
                    else:
                        result_str = result_str + " "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "G":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 5) and (column < 4 or row > 2) and (row != 0 and row != 6)) or (
                            ((row == 6 or row == 0 or (column != 1 and row == 3))) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "H":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 6)) or ((row == 3) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "I":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((column == 3 and (row != 0 and row != 6)) or (
                            (row == 0 or row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "J":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((column == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6 or row == 5) and (
                            (2 <= column <= 3 or row != 6) and (column == 1 or row != 5)) and (
                                                                              column > 0 and column < 7))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "K":
            result_str = "";
            i, p = 0, 4
            x, q = 4, 2
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0)) or (
                            (row == i and column == x) or (row == p and column == q) or (column == 3 and row == 5) or (
                            column == 4 and row == 6) and (column > 0 and column < 5))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
                i += 1
                x -= 1
            print(result_str)
        elif n[i] == "L":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((column == 0) or ((row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "M":
            result_str = "";

            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 6)) or (
                            (row == 1 and column == 1) or (row == 2 and column == 2) or (column == 3 and row == 3) or (
                            column == 4 and row == 2) or (column == 5 and row == 1) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "N":
            result_str = "";

            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 6)) or (
                            (row == 1 and column == 1) or (row == 2 and column == 2) or (column == 3 and row == 3) or (
                            column == 4 and row == 4) or (column == 5 and row == 5) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "O":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 6) and (row != 0 and row != 6)) or (
                            (row == 0 or row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str);
            result_str = ""
        elif n[i] == "P":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 5) and (column < 4 or row < 4)) or (
                            (row == 3 or row == 0) and (column > 0 and column < 5))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "Q":
            for row in range(8):
                for col in range(12):
                    if ((col == 0 or col == 4) and (row > 0 and row < 6)) or (
                            (row == 0 or row == 6) and (col > 0 and col < 4)) or (
                            (row == 5 and col == 1) or (row == 7 and col == 3)):
                        print("* ", end="")

                    elif ((col == 6 or col == 10) and (row > 0 and row < 6)) or (
                            (row == 0 or row == 6) and (col > 6 and col < 10)) or (
                            (row == 5 and col == 7) or (row == 7 and col == 9)):
                        print("* ", end="")
                    else:
                        print(end="  ")

                print()
        elif n[i] == "R":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 1 or (column == 6 and row < 4) or (column == 3 and row == 4) or (
                            column == 4 and row == 5) or (column == 5 and row == 6)) and (row != 0 and row != 3)) or (
                            (row == 0 or row == 3) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "S":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((((column == 0 and row < 4) or (column == 6 and row > 3)) and (row != 0 and row != 6) and (
                            row != 3)) or (((row == 0 or row == 6) or (row == 3)) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str);
            result_str = ""
        elif n[i] == "T":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((column == 3 and (row != 0 and row != 6)) or (row == 0 and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "U":
            result_str = "";
            for row in range(0, 7):
                for column in range(0, 7):
                    if (((column == 0 or column == 6) and (row != 0 and row != 6)) or (
                            (row == 6) and (column > 0 and column < 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
            print(result_str)
        elif n[i] == "V":
            result_str = "";
            i, x, y = 0, 0, 12
            for row in range(0, 7):
                for column in range(0, 14):
                    if ((((row == i and column == x) or (column == y and (6 > row == i))) and (
                            column >= 0 and column < 15))):
                        result_str = result_str + "*"
                    else:
                        result_str = result_str + " "
                result_str = result_str + "\n"
                i += 1
                x += 1
                y -= 1
            print(result_str);
            result_str = ""
        elif n[i] == "W":
            result_str = "";
            i, x, y = 0, 0, 12
            a, b = 12, 24
            for row in range(0, 7):
                for column in range(0, 28):
                    if ((((row == i and column == x) or (column == y and (6 > row == i)) or (
                            row == i and column == a) or (column == b and (6 > row == i))) and (
                                 column >= 0 and column < 29))):
                        result_str = result_str + "*"
                    else:
                        result_str = result_str + " "
                result_str = result_str + "\n"
                i += 1
                x += 1
                y -= 1
                a += 1
                b -= 1
            print(result_str);
            result_str = ""
        elif n[i] == "X":
            result_str = "";
            i, x, y = 0, 0, 6
            for row in range(0, 7):
                for column in range(0, 7):
                    if (
                    (((row == i and column == x) or (column == y and (row == i))) and (column >= 0 and column < 7))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
                i += 1
                x += 1
                y -= 1
            print(result_str);
            result_str = ""
        elif n[i] == "Y":
            result_str = "";
            i, x, y = 0, 0, 6
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((((row == i and (4 > column == x)) or (column == y and (row == i))) and (
                            column >= 0 and column < 7))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
                i += 1
                x += 1
                y -= 1
            print(result_str);
            result_str = ""
        elif n[i] == "Z":
            result_str = "";
            a, b = 6, 0
            for row in range(0, 7):
                for column in range(0, 7):
                    if ((((row == 0 or row == 6) or (column == a and row == b)) and (column >= 0 and column <= 6))):
                        result_str = result_str + "* "
                    else:
                        result_str = result_str + "  "
                result_str = result_str + "\n"
                a -= 1
                b += 1
            print(result_str);
            result_str = ""


printname()
input()
