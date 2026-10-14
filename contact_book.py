contact={'Vivek':9123456700,
         'Shubham':9881110948,
         'Mahesh': 9881110949,
         'Sahil':9881110988,
         'Krish':9881110234,
         'Aryan':9881119876,
         'Sarthak':9881123456,
          'Pritish':9865123456,
          'Aashish':9881893456,
          'Shruti':9881123456,
          'Riya':9431123456,
          'Vaishnavi':9671123456,
          'Avanti':9981123456,
          'Sneha':9441123456,
          'Umakanth':9331123456,
          'Sumit':9885553456,
         'Harshit':9833323456,
         'Om':9881123777
                }

print(contact)
print('count :',len(contact))
contact['vikrant']=9356681209
print(contact)
print('count :',len(contact))
              
print(contact['Om'])

contact.update({'Om':1122334455})
print(contact['Om'])
print(contact)
print(contact.popitem())
print(contact.pop('Sahil'))

for i in contact.items():
    print(i)
    
