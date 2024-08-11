#pip install psycopg2--binary

import psycopg2
import pandas as pd
from database import connect
from sqlalchemy import create_engine, String, Text
#create table

def create_table(table_headings):
    conn=connect()
    cursor=conn.cursor()
    for table_name in table_headings:
        cursor.execute(f"CREATE TABLE {table_name}1 (question varchar(200), speak varchar(200), details varchar(200), additional_info varchar(200), images bytea);")
        conn.commit()
    conn.close()
    print('Tables successfully created.')
    
def csv_todf(filename):
    df= pd.read_csv(filename)
    df= df[["question", "speak", "details", "additional_info","images"]]
    print(df)
    return df

def df_totable(df, tablename):
    
    #establish connections
    conn_string = 'postgresql+psycopg2://postgres:your_password@localhost:5432/Instructions_Caterpillar' #replace with DB password
  
    db = create_engine(conn_string) 
    conn = db.connect()  
    df.to_sql(f'{tablename}', conn, if_exists= 'replace') 
    conn.commit()
    

#export from csv to table
if __name__=='__main__':
    table_headings= ['Header', 'Battery', 'Brakes', 'Engine', 'Exterior', 'Tires', 'Voice_of_Customer' ]
    df= csv_todf(r"SmartAssist questions\battery_new.csv")
    df_totable(df,'battery1')
   