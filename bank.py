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
        try:
          amount+10
        except TypeError:
          return f"please enter amount in figures"

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
        try:
          withdraw_amount+10
        except TypeError:
           return f"please enter amount in figures"
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
        try:
          borrow_amount+10
        except TypeError:
          return f"please enter amount in figures"

        loan=borrow_amount- self.loanlimit
        loanfees=0.05*borrow_amount
        if borrow_amount>0: 
          return " quallified for the loan"
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
       try:
         amount+10
       except TypeError:
          return f"please enter amount in figures"

       
       
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
          self.loan=0
          transction={
          "borrow_amount":amount,"balance":self.balance,"narration":"You have successfully repaid",
          "time":datetime.now(),}
          
          self.transactions.append(transction)
          return "you have an existing loan balance"

     def transfer(self,amount,account):
        try:
         amount+10
        except TypeError:
          return f"please enter amount in figures"
        amount>0
        loanfee=amount*0.05
        total=amount+loanfee
        if total>self.balance:
          return f"your balances is {self.balance}  you need{total} inorder to transfer"
        else:
          self.balance=total
          account.deposite(amount)
          return f"you have sent{amount} to{account.name} and your balance is{self.balance}"
class MobileMoneyAccount(Account):
     def __init__(self,name,phonenumber,service_provider):
        Account.__init__(self,name,phonenumber)
        self.service_provider=service_provider

     def buy_airtime(self,amount):
       amount>0
       amount<=self.balance
       amount-=self.balance
       transction={
            "withdraw_amount":amount,"balance":self.balance,"narration":"You have withdrawn",
            "time":datetime.now(),}
          
       self.transactions.append(transction)
       return f"Hello {self.name} confirm that you have bought airtime of{amount}  and your new balance is{self.balance}"
           




       
       
    

         

        
    
     

                


           

   





        









