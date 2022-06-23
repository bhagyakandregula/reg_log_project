import sqlite3
conn=sqlite3.connect("my_db")
print("Enter delete record name ")
en=input()
query=" delete from log_reg_table where name='" + en + "'"
conn.execute(query)
conn.commit()
conn.close()