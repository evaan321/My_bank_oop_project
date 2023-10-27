from random import randint

class Bank:

    def __init__(self,name) -> None:
        self.name = name
        self.bank_balance=1000
        self.ac_holders = {}
        self.loan_limit = 2
        self.loan_amount = 0

    def loan_off(self):
        self.loan_limit =-1

    def loan_on(self):
        self.loan_on = 2
        
        






class User():
    def __init__(self , name, email , acType) -> None:

        self.name = name
        self.email = email
        self.acType= acType

        self.balance = 0
        self.acNumber = str(randint(1,10000))+name[0:3]
      
        self.loan_taken = 0

        self.transHistory = []

    def deposit_money(self,deposit):
        self.balance +=deposit
        self.transHistory.append(f'Deposited {deposit} tk')
        print(f'Deposited {deposit} Taka Now Balance is {self.balance}')

    def withdraw_money(self,withdraw):
        if withdraw > self.balance:print("Withdrawal amount exceeded")
        else :
            self.balance -=withdraw 
            print(f'Balance after withdraw is {self.balance}')
            self.transHistory.append(f'withdraw {withdraw} tk')

    def check_balance(self):
        print(f'Your Account Balance is {self.balance}')

    def transaction_history(self):
        print(self.transHistory)

    







        