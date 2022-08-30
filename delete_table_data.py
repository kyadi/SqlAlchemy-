from sqlalc import Test, session

table = Test #test table object







#__DELETING__

#query by filtering what you want to update
data3 = session.query(table).filter(Test.title == 'first line').first()

#delete the data
session.delete(data3)

#commit or save the changes
session.commit()



