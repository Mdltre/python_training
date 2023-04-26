class BankAccount(object):
    interest_rate = 0.3
    
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self,num):
        self.balance += num
        print(self.balance)
        
    def withdraw(self,num):
        if self.balance >= num:
            self.balance -= num
            print("Amount of " + str(num) + " has been withdrawn.")
        elif self.balance < num:
            print("You have reached your overdraft limit.")
        else:
            print("Not enough balance!")
            
    def add_interest(self):
        interest = (self.balance * self.interest_rate) + self.balance
        print("Interest with the amount of " + str(interest) + " added.")

class StudentAccount(BankAccount):
            
    def withdraw(self,num):
        if self.balance >= num:
            self.balance -= num
            print("Amount of " + str(num) + " has been withdrawn.")
            print(self.balance)
        elif self.balance < num:
            print("You have reached your overdraft limit.")
        else:
            print("Not enough balance!")
            
# bank = BankAccount("Test", 90000, 300)

# bank.deposit(100)
# bank.withdraw(200)
# bank.add_interest()

# student = StudentAccount("Stud", 10000,500)

# student.deposit(100)
# student.withdraw(300)
# student.add_interest()