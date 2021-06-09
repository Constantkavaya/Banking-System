from datetime import  date, datetime, time
class Account:
     def __init__(self,name,phone):
         self.name=name
         self.phone=phone
         self.balance=0
         self.transaction=10
         self.loanlimit=34000
         self.loan=0
         self.loanfees=5 
         self.transactions=[]
         self.repay=0
         self.repayed=[]
     def deposite(self,amount):

         if amount<=0:
            print ("please deposite a valid amount")

         else:
          self.balance+=amount
          transction={
            "amount":amount,"balance":self.balance,"narration":"You have deposited",
            "time":datetime.now(),}
          
          self.transactions.append(transction)
          return f"Hello {self.name} you have deposited{amount} your new balance is{self.balance}"
     def withdraw(self,withdraw_amount):
         total=withdraw_amount+self.transaction

         if withdraw_amount<=0:
           return "valid amount"

         elif total<=self.balance:
           return "insufficient amount"
       
         else:
           self.balance==total
           transction={
            "withdraw_amount":withdraw_amount,"balance":self.balance,"narration":"You have withdrawn",
            "time":datetime.now(),}
          
           self.transactions.append(transction)
           return f"Hello {self.name} you have deposited{withdraw_amount} your new balance is{self.balance}"
           
     def borrow(self,borrow_amount) :
         loan=borrow_amount- self.loanlimit
         loanfees=0.05*borrow_amount
         if borrow_amount>0: 
             return "Not quallified for the loan"
         elif loan<=34000 :    
             return "try again later"  
         else :
             self.balance=loan
             transction={
            "borrow_amount":borrow_amount,"balance":self.balance,"narration":"You have borrowed",
            "time":datetime.now(),}
          
             self.transactions.append(transction)
           
             return f"Hi {self.name} you are not allowed to borrow{borrow_amount} since you outstanding balance is{self.balance}" 

     def get_statement(self):
       for transaction in self.transactions:
         amount=transaction["amount"]
         narration=transaction["narration"]
         balance=transaction["balance"]
         time=transaction["time"]
         date=time.strftime("%D")
         print("f{date}...{narration}...{amount}...{balance}")
     

     def repay_loan(self,amount):
       
        if amount<0:
          return "you  are not allowed to pay"
        elif amount> self.loan:
          minus=amount-self.loan
          self.balance+=minus
          transction={
          "borrow_amount":amount,"balance":self.balance,"narration":"You have successfully repaid",
          "time":datetime.now(),}
          
          self.transactions.append(transction)
          return "you are awesome"
        else:
          self.loan-=amount
          transction={
          "borrow_amount":amount,"balance":self.balance,"narration":"You have successfully repaid",
          "time":datetime.now(),}
          
          self.transactions.append(transction)
          return "you have an existing loan balance"

         

        
    
     

                


           

   





        









