import sqlite3

conn = sqlite3.connect('piet_Data_base.db')
fetchQuerry = '''select * from student'''
cur = conn.cursor()
cur.execute(fetchQuerry)
result = cur.fetchall()
i=0
for row in result:
    print(i,' ',row)
    i+=1
cur.close()
conn.close()