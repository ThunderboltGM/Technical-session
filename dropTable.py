import sqlite3
conn = sqlite3.connect('piet_Data_base.db')
deletionQuerry = '''drop table student'''
cur = conn.cursor()
cur.execute(deletionQuerry)
print("table deleted successfully")
cur.close()
conn.close()