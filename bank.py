class Account:
    def __init__(self,name,phone_number,account_number,id):
        self.name=name
        self.phone_number=phone_number
        self.account_number=account_number
        self.id=id
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
    
    def withdraw (self,amount):
        self.amount=amount
        if amount>self.balance:
            return f"Dear customer, you have insuffient funds for this withdraw"
        elif amount<=0:
            return f"Dear customer, you can't withdraw zero amount "            
        else:
            
             self.balance -=amount
             self.withdrawals.append(amount)
        return f"Thank you for the withdraw, your new balance is  {self.balance}"
    def deposit(self,amount):
        self.amount=amount
        
        if amount<=0:
            return f"deposit amount must be greater than zero(0)"
        else:
             self.balance+=amount
             self.deposits.append(amount)
            
        return f"Thankyou for depositing ,your new balance is  {self.balance}"
        
    def deposit_statement(self):
        for x in self.deposits:
            print (x)
    def withdraw_statement(self):
        for y in self.withdrawals: 
            print(y)
    def transaction(self):
         self.balance -=self.amount+100
         return self.balance  
         
    def current_balance(self):
        return f" Your current balance is  {self.balance}" 
  
        
            