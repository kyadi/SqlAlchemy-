from sqlalc import Test, session



#creating an instance in the table, the args are the data to be saved
test12 =Test(title='first line', adult=True)
test13 =Test(title='sec line', adult=True)
test14 =Test(title='quat line', adult=True)


session.add(test12)#for one instance

session.add_all([test13,test14])#for multiple addition

session.commit()