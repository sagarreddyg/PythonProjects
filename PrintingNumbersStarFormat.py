def Print1():
    result_str = ""
    for row in range(7):
        for col in range(7):
            if (col == 3)or (row == 1 and 1 < col < 3) or (row == 2 and col == 1) or (row == 6 and 1 <= col <= 5):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)
Print1()
