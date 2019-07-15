import sqlite3


conn = sqlite3.connect('test.db')

curss = conn.cursor()


#execute 是执行的意思
#curss.execute('create table user (id varchar(7) primary key ,name varchar(20))')
#curss.execute('insert into user(id,name) values (\'001\',\'march\')')



curss.close()
conn.commit()
