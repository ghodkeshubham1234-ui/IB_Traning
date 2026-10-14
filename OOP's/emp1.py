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
