"""
class demo:
    collage="ISBM" # class variable
    location='pune'
    def fee(self,fees,additional_charge):
        self.fees=fees
        self.fees=self.fees + additional_charge
    def show(self):
        print('Collage Name :',self.collage)
        print('Location :',self.location)
        print('Total fees :',self.fees)
dm=demo()
#dm.fees=42000
#dm.additional_charge=15000
dm.fee(42000,15000)
dm.show()
"""
class demo:
    def __init__(self,name,contact,collage,location):
        self.name=name
        self.contact=contact
        self.collage=collage
        self.location=location
      
    def fee(self,fees,additional_charge):
        self.fees=fees
        self.fees=self.fees + additional_charge
    def show(self):
        print('Student Name :',self.name)
        print('Contact Number :',self.contact)
        print('Collage Name :',self.collage)
        print('Location :',self.location)
        print('Total fees :',self.fees)
dm=demo("Shubham",9881110948,"ISBM",'pune')
#dm.fees=42000
#dm.additional_charge=15000
dm.fee(42000,15000)
dm.show()

