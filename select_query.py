import sqlite3
conn=sqlite3.connect("my_db")
cur=conn.cursor()
query=" select * from log_reg_table"
cur.execute(query)
data=cur.fetchall()
print("type of data is :",type(data))
print("\n")
for d in data:
    print("name:",d[0])
    print("contact_no:",d[1])
    print("company_name:",d[2])
    print()
cur.close()
conn.close()
