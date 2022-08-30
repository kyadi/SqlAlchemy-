from sqlalchemy import create_engine,Float, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


#connecting to a database database
db_eng = create_engine('mysql+pymysql://root:@localhost:3306/testdb')


#binding to the database
session = scoped_session(sessionmaker(bind=db_eng))


Base = declarative_base()

#creating a table
class Test(Base):
    __tablename__ ='test1'
    id = Column(Integer(), primary_key=True)
    title = Column(String(500))
    adult = Column(Boolean(), default=False)

#this is the migration
Base.metadata.create_all(db_eng)


#creating an instance in the table, the args are the data to be saved
test12 =Test(title='first line', adult=True)
