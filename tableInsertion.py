import sqlite3
conn = sqlite3.connect('piet_Data_base.db')
tableInsertionQuerry = '''insert into student(name,password)values("gaurav",5529)'''
cur = conn.cursor()
cur.execute(tableInsertionQuerry)
print("values inserted into the table successfully")
cur.close()
conn.close()