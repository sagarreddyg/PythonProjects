num1 = int(input("enter your range from printing even number's : "))
num2 = int(input("enter your range To printing even number's : "))
coun = 0
for i in range(num1, num2+1):
  if i % 2 == 0:
    print(i, end=",")
    coun += 1

print("\nTotal number of even number between {} to {} is {}".format(num1, num2, coun))
input()
