f = open("dude","r")

myList = []
for line in f:
   myList.append(line)

nums = []
for i in myList:
    nums.append(int(i))

flag = ""
for number in nums:
    flag += chr(number)

print(flag)
