class Account:
     def __init__(self,name,phone):
         self.name=name
         self.phone=phone
         self.balance=0
         self.transaction=10
         self.loanlimit=34000
         self.loan=0
         self.loanfees=5 
     def deposite(self,amount):

         if amount<=0:
            print ("please doposite a valid amount")

         else:
          self.balance+=amount
          return f"Hello {self.name} you have deposited{amount} your new balance is{self.balance}"
     def withdraw(self,withdraw_amount):
         total=withdraw_amount+self.transaction

         if withdraw_amount<=0:
           return "valid amount"

         elif total<=self.balance:
           return "insufficient amount"
       
         else:
           self.balance==total
           return f"hello {self.name} you  have successfully borrowed{withdraw_amount} and you account balance is{self.balance}"
     def borrow(self,borrow_amount) :
         loan=borrow_amount- self.loanlimit
         loanfees=0.05*borrow_amount
         if borrow_amount>0: 
             return "Not quallified for the loan"
         elif loan<=34000 :    
             return "try again later"  
         else :
             self.balance=loan
             return f"Hi {self.name} you are not allowed to borrow{borrow_amount} since you outstanding balance is{self.balance}"    
           

   





        









