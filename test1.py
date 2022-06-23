import sqlite3
conn = sqlite3.connect("my_db")
print("Enter update employee name")
en = input()
print("Enter update employee contact number")
ecn = input()
query="update log_reg_table set contact_no=" + ecn +" where name='" +en+"' "
conn.execute(query)
conn.commit()
conn.close()
