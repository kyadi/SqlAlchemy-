from sqlalc import Test, session

table = Test #test table object


#query all data in table
data = session.query(table)
for x in data:
    print(x.id, x.title)


#query by orderby
data1 = session.query(table).order_by(Test.title)
for x in data1:
    print(x.id, x.title)


#query by filtering
data2 = session.query(table).filter(Test.title == 'quat line')
for x in data2:
    print(x.id, x.title)


#counting  data 
data_count = session.query(table).count()
print(data_count)