user_input = input("Enter string : ")

def occurrences_counter(str):
    count = dict()
    str = str.lower()
    nopunc = ''.join(x for x in str if x.isalnum() or x.isspace())
    words = nopunc.split()
    
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
            
    return count
            
print(occurrences_counter(user_input))