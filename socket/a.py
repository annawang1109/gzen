import pymysql
conn = pymysql.connect(host = '127.0.0.1', port = 3306, user='root', passwd='root123456', db='znoqa')
cursor = conn.cursor()
cursor.execute("select * from product_type")
user_list = cursor.fetchall()
print(len(user_list))