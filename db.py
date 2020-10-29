import sqlite3

conn=''

# def open_connection():
#    return sqlite3.connect('pythondb.db')

# def close_connection():
#    return conn.close()



def get_device_list():
   conn=sqlite3.connect('pythondb.db')
   cursor = conn.execute("select name from devices")
   data=[]
   i=0
   for row in cursor:
      #data.__add__(row[i])
      data.insert(i,row[i])
      #i+1
   conn.close()
   return data

def pingdata(sel):
   conn = sqlite3.connect('pythondb.db')
   print("Printing sel on db block: ",sel)
   print("Printing query in pingdata block: ","select * from devices where name="+sel+"")
   cursor = conn.execute("select * from devices where name='"+sel+"'")
   data = {}
   i = 0
   for row in cursor:
      data={'device':{'id':row[0],'ip_addr':row[1],'mac':row[2],'name':row[3],'username':row[4],'password':row[5]}}
      i + 1
   conn.close()
   return data

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");


# cursor = conn.execute("SELECT * from devices")
# for row in cursor:
#    print ("ID = ", row[0])
#    print ("IP Address = ", row[1])
#    print ("MAC-Address = ", row[2])
#    print ("Name = ", row[3])
#    print("Username = ", row[4])
#    print("Password = ", row[5],'\n')


#print('opened database successfully')

#conn.commit()
print ("Records created successfully")
