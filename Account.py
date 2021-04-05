class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
        
    def __str__(self):
        return('Account owner: {} \nAccount balance {}'.format(self.owner, self.balance))
        
    def deposit(self, deposit_amt):
        
        self.balance = self.balance + deposit_amt
        print('You have been credited with {} and your current balance is {}'.format(deposit_amt, self.balance))

        return self.balance
        
    def withdraw(self, withdraw_amt):
         
            if withdraw_amt > self.balance:
                return ('Funds Unavailable, You have only {} in your account'.format(self.balance))
            else:
                self.balance = self.balance - withdraw_amt
                return ('Withdrawal Accepted and your current balance is {}'.format(self.balance))
    
    def accountbalance(self):
        return self.balance

print("Enter owner name:")
d = input()
# print(i)
# n=int(input())
w = Account(d)
print("enter data")
while(True):
    s = input().split(" ")
    if(s[0]=="exit"):
        break
    if(s[0] == 'credit'):
        print(w.deposit(float(s[1])))
    elif(s[0] == 'debit'):
        print(w.withdraw(float(s[1])))
    elif(s[0] == 'checkBalance'):
        print(w.accountbalance())


# class Bank:
#     def _init_(self):
#         self.balance = 0.0
#         print ("The account is created")
        
#     def deposit(self):
#         amount = float(input("Enter the amount to be deposit: "))
#         self.balance = self.balance + amount
#         print ("Deposit is successful and the balance in the account is %f" % self.balance)
    

#     def withdraw(self):
#         amount = float(input("Enter the amount to withdraw: "))
#         if (self.balance >= amount):
#             self.balance = self.balance - amount
#             print ("The withdraw is successfull and balance is %f" % self.balance)
#         elif(amount>self.balance):
#             # self.balance=self.balance-amount
#             print("withdraw money exceeded available balance")
#         else:
#             print ('Insuficient Balance')
    


#     def checkbalance(self):
#         print ("Balance in the acount is %f" % self.balance)

# acc = Bank()       
# while(True):
   
#     print("please enter your choice")
#     s=input()
#     if(s=="exit"):
#         break
#     if(s=="deposit"):
#         acc.deposit()
#     elif(s=="withdraw"):
#         acc.withdraw()
#     elif(s=="checkbalance"):
#         acc.checkbalance()
#     else:
#         print("Invalid")