import sqlite3
conn = sqlite3.connect('piet_Data_base.db')
tableInsertionQuerry = '''insert into student values(?,?)'''
cur = conn.cursor()
value = ['gaurav',5529]
cur.execute(tableInsertionQuerry,value)
conn.commit()
print("values inserted into the table successfully")
cur.close()
conn.close()