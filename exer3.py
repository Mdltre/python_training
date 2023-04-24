name1 = input("Enter Name 1: ")
name2 = input("Enter Name 2: ")

n1 = name1.replace(" ","").lower()
n2 = name2.replace(" ","").lower()

count1 = 0
count2 = 0

for i in n1:
    if i in n2:
        count1 += 1
for i in n2:
    if i in n1:
        count2 += 1

finalcount = count1 + count2

def checkflmes(int):
    res = ["FRIENDS", "LOVE", "ACQUAINTANCES", "MARRIAGE", "ENEMY", "SIBLINGS"]
    check = int % 6 - 1
    return res[check]
        

print("Result for "+ name1 +" ==> " +str(checkflmes(count1)))
print("Result for "+ name2 +" ==> " +str(checkflmes(count2)))
print("FINAL RESULT ==> " + str(checkflmes(finalcount)))