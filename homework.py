#requirments - iteam code and price
'''wap  that has a class store which keeps a record of code and price of each product display a menu of all products 
to the user and prompt them to enter the quantity of each item required and finally geenrate a bill and display total amount'''

class Store:
    iteamcode=0
    nameofproduct=[]
    quantity=0
    price=0
    totalprice=0

def __init__(self,i,sn,q,p,tp):
        self.iteamcode=i
        self.snameofproduct=sn
        self.quantity=q
        self.price=p
        self.totalprice=tp
