class Bank_V1:
    bank_name="SBI"
    bank_roi=6
    bank_addres="Bangarupeta"
    
    def __init__(self,name,age,occupation,bal,pin):
        self.customer_name=name
        self.customer_age=age
        self.customer_occupation=occupation
        self.balance=bal
        self.pin=pin

    @classmethod
    def display_bank_details(cls):
        print("bank name : ",cls.bank_name)
        print("bank roi : ",cls.bank_roi)
        print("bank adress : ",cls.bank_addres)

    def withdra(self):
        amount=self.withdra_amount()
        pin=self.checking_pin()
        if pin==self.pin:
            print("your balance is : ",self.balance)
            if amount<=self.balance:
                print("withdrawal succesful")
                self.balance-=amount
                print("your current balance is : ",self.balance)
            else:
                print("in sufficient balance")
        else:
            print("incorrect pin")

    def holders_details(self):
        print("customer name : ",self.customer_name)
        print("customer age : ",self.customer_age)
        print("customer occupation : ",self.customer_occupation)
        print("customer balance is : ",self.balance)
        
    @staticmethod
    def withdra_amount():
        amount = int(input("enter withdrawal amount : "))
        return amount
    
    @staticmethod
    def checking_pin():
        pin=input("enter your pin : ")
        return pin
    

class Bank_V2(Bank_V1):
    bank_roi=10
    bank_addres="Bangladesh"
    bank_mobile=7660089410
    
    def __init__(self,name,age,occupation,bal,pin,adhar,pan):
        super().__init__(name,age,occupation,bal,pin)
        self.adhar=adhar
        self.pan=pan

    def deposit(self):
        amount=self.getwithdra_amount()
        print("your current balance is : ",self.balance)
        self.balance+=amount
        print("your balance is",self.balance)
        print("deposit succesfull thank you for visiting")
 
    @classmethod
    def display_bank_details(cls):
        super().display_bank_details()
        print("bank mobile : ",cls.bank_mobile)

    def change_pin(self):
        pin=self.changing_pin()
        self.pin=pin
        print("your paswors is changed succesfully")

    def holders_details(self):
        super().holders_details()
        print("customer adhar is : ",self.adhar)
        print("customer pan is : ",self.pan)
        
    @staticmethod
    def getwithdra_amount():
        amount=int(input("enter deposit amount : "))
        return amount

    @staticmethod
    def changing_pin():
        pin=input("enter your new pin : ")
        return pin
    
    
        
muni=Bank_V2("yashu",19,"student",7800,"yashu149",5665466,"GDFGD5")

muni.display_bank_details()
muni.withdra()
muni.change_pin()
muni.withdra()
muni.holders_details()
muni.deposit()
