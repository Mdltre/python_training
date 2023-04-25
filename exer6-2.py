def recsort(needsort, sortedlist):
    
    if len(needsort) == 0:
        return sortedlist
    else:
        x = min(needsort)
        needsort.remove(x)
        sortedlist.append(x)
        return recsort(needsort,sortedlist)

needsort = [98798,0,7,9,5,3,4,52,36,4236,5734,24]
sortedlist = []

print(recsort(needsort, sortedlist))