from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
import uuid
import sqlalchemy as db
import pandas as pd
from client import call_server

SAMPLE_SIZE=100
RUN_SIZE=50


def generate_uuid():
    uuid_obj=uuid.uuid4()
    return uuid_obj.hex

def save_list_of_timings(l=[]):
    engine = db.create_engine('sqlite:///timings_home_lan.db') 
    df=pd.DataFrame(l)
    df.rename(columns={0: 'timing'}, inplace=True)
    df['set_id']=generate_uuid()
    df.to_sql('timings', engine, if_exists='append',index=False)
    return #niets


def get_list_of_timings(user='000000',password='test',test_chararcter='S',sample=SAMPLE_SIZE,run=RUN_SIZE,debug=False):
    resultlist=[]
    for r in range(0,run):
        if debug:
            print(f"Ronde {r}")
        for s in range(0,sample):
            if debug:
                print(f"Ronde {s}")
            result, time = call_server(username=user,password=password)
            if result[0]==test_chararcter:
                resultlist+=[time]
                if debug:
                    print(f"Tijd {time} meegenomen op de lijst")
                else:
                    print(f"Ronde {r} ronde {s} tijd meegenomen {time} ", end='\r')
            else:
                print(f"Ronde {r} ronde {s} mogelijk probleem {result} ")
    return resultlist




print("the data way")
save_list_of_timings(get_list_of_timings())


  

  
# # Define the profile table 
  
# # database name 
# profile = db.Table( 
#     'timings',                                         
#     metadata_obj,  
#     db.Column('ID',db.Integer, primary_key=True),                                   
#     db.Column('set_id', db.String(32)),   
#     db.Column('timing', db.Float),                     
#     db.Column('char', db.String),                 
# ) 
  
# # Create the profile table 
# metadata_obj.create_all(engine) 