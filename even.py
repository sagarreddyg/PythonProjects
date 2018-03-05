num = int(input("enter your range for printing even number's : ")
coun = 0
for i in range(1, num+1):
  if i % 2 == 0:
    print(i)
	coun += 1
print("Total number of even number between the 1 and {} is {}".format(num, coun)

