from sqlalc import Test, session

table = Test #test table object



#__UPDATING__

#query by filtering what you want to update
data2 = session.query(table).filter(Test.title == 'quat line').first()

#update the data
data2.title = 'quat for 3'

#commit or save the changes
session.commit()








