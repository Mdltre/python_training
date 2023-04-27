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
        for element in range(2, num):
            if num % element == 0:
                return False
        return True
    
div = PrimeNumberDigit(13)
print(next(div))
print(next(div))
print(next(div))
print(next(div))
print(next(div))