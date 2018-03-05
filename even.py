num = int(input("enter your range for printing even number's : "))
coun = 0
for i in range(1, num+1):
  if i % 2 == 0:
    print(i, end=",")
    coun += 1

print("\nTotal number of even number between 1 to {} is {}".format(num, coun))
