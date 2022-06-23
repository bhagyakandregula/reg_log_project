import sqlite3
conn = sqlite3.connect("my_db")
'''we have to write the statements to fire required query into the database tables.
#like this we can create any numbers of database.
#strictly remember that, this is the best and easy process to create new database in sqlite3 studio'''
print("Enter employee name")
en = input()
print("Enter employee contact number")
ecn = input()
print("Enter employee  company name")
ec = input()
query = " insert into log_reg_table(name,contact_no,company_name) values ('" + en + "'," + ecn + ", '" + ec +"')"
conn.execute(query)
conn.commit()
conn.close()
print("data inserted")
