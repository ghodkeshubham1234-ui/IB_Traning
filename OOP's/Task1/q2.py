class tea_order:
    print('='*60)
    print('           TEA BREAK             ')
    print('='*60)
    stall_name="TEA BREAK"
    total_order=0
    def __init__(self,customer_name,tea_type,quantity):
        self.customer_name=customer_name
        self.tea_type=tea_type
        self.quantity= quantity
        tea_order.total_order += quantity
        
    def display(self):
        
        print( "Welcome  at ",self.stall_name)
        print('Customer Name :',self.customer_name)
        print('Customer Name :',self.tea_type)
        print('Customer Name :',self.quantity)
        
        print("THANK YOU ! Visit again....! ")
        print('*'*50)
        
t=tea_order('om','ginger tea',5)
t.display()
    
t1=tea_order('sahil','no sugar tea',2)
t1.display()

t2=tea_order('yash','hurble tea',3)
t2.display()

t3=tea_order('shubham','black tea',4)
t3.display()
print('Today order  :',tea_order.total_order)
