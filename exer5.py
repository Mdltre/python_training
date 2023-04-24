str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
str3 = input("Enter string 3: ")

with open("exer5.txt", "a") as f:
    f.write(str1 + "\n")
    f.write(str2 + "\n")
    f.write(str3 + "\n")
    
with open("exer5.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
lines.sort()
    
for word in lines:
    print(word)
