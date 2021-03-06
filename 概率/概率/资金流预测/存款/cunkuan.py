import MySQLdb
from get_time import *
import matplotlib.pyplot as plt
import cPickle as pickle

conn = MySQLdb.connect(host = "localhost",user = 'root',passwd = 'zhao0108',db = 'zhao')
cursor = conn.cursor()

sql = "select report_date,tBalance from balance_2014"
ss = "  where (Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' or SubString(report_date,1,6) = '201408')"
sql = sql + ss
cursor.execute(sql)
rows = cursor.fetchall()
key_time = get_time('20140601')

total_money = {}
i = 0
for row in rows:
    i = i + 1
    if i % 10000 == 0:
        print i
    report_date,tBalance = row
    day = (get_time(report_date) - key_time).days
    if day not in total_money.keys():
        total_money[day] = 0
    total_money[day] += tBalance
print total_money
f = file("../data/total.pkl",'wb')
pickle.dump(total_money,f)
f.close()
X = []
Y = []
for key in total_money.keys():
    X.append(key)
    Y.append(total_money[key])

plt.figure(1)
plt.plot(X,Y)
plt.show()


conn.close()
cursor.close()




