def my_range(start,stop):
    current = start
    while current< stop:
        yield current
        current += 1
        
nums = my_range(1,6)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
    