import psycopg2

def connect():
    conn= psycopg2.connect(database="Instructions_Caterpillar",
                        host="127.0.0.1",
                        user="postgres",
                        password="your password here", #replace with DB password
                        port=5432)
    if conn:
        print('Connection Established with database.')
    else:
        print("connection has not been established.")
    return conn


def get_rows():
    row_list=[]
    conn=connect()  
    curr=conn.cursor()
    curr.execute('SELECT * FROM tyre')
    data=curr.fetchall()

    for row in data:
        row_list.append(row)
        print(row)
        
    conn.close()
    return row_list
    
def retrieve_question():
    conn=connect()
    curr=conn.cursor()
    curr.execute("SELECT * FROM tyre")
    data= curr.fetchall()
    return data

def get_column_names():
    colnames_list=[]
    conn=connect()
    curr=conn.cursor()
    curr.execute("Select * FROM tyre LIMIT 0")    
    colnames = [desc[0] for desc in curr.description]
    for column in colnames:
        print(column)
        colnames_list.append(column)
    conn.close()
    return colnames_list

def insert_val(text, q):
    conn=connect()
    curr=conn.cursor()
    if(text):
        curr.execute(f"UPDATE tyre SET additional={text} WHERE val=1 AND question='{q}'")
    conn.commit()
    conn.close()
    
def set_good(q):
    conn=connect()
    curr=conn.cursor()
    curr.execute(f"UPDATE tyre SET good=1 WHERE question='{q}'")
    conn.commit()
    conn.close()
    
def set_bad(q):
    conn=connect()
    curr=conn.cursor()
    curr.execute(f"UPDATE tyre SET bad=1 WHERE question='{q}'")
    conn.commit()
    conn.close()
    
def set_okay(q):
    conn=connect()
    curr=conn.cursor()
    curr.execute(f"UPDATE tyre SET okay=1 WHERE question='{q}'")
    conn.commit()
    conn.close()
    
def set_additional(text, q):
    conn=connect()
    curr=conn.cursor()
    if(text):
        curr.execute(f"UPDATE tyre SET additional='{text}' WHERE question='{q}'")
    conn.commit()
    conn.close()
    

if __name__== '__main__':
    get_column_names()
    get_rows()
    

    