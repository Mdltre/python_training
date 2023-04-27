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
        
        
class PrimeNumberDigit:
    
    def __init__(self, num):
        self.num = num
        self.cur = num
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if str(self.num) in str(self.cur) and self.is_prime(self.cur):
                prime_num = self.cur
                self.cur += 1
                return prime_num
            else:
                self.cur += 1

    def is_prime(self,num):
        if num < 2:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        return True
    
div = PrimeNumberDigit(13)
next(div)