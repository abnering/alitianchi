import cPickle as pickle
import csv
import MySQLdb

conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'zhao0108',db = 'zhao')
cursor = conn.cursor()

sql = "select tBalance from test_2014_08"
ss = "  where report_date = '20140831'"
sql += ss;
cursor.execute(sql)
rows = cursor.fetchall()
total_money = 0;
for row in rows:
    tBalance, = row
    total_money += tBalance
conn.close()
cursor.close()
total_money = total_money/100

f = file('result.pkl','rb')
result_first = pickle.load(f)
f.close()

print total_money
print result_first
result_2 = { }
for key in result_first.keys():
    if key not in result_2.keys():
        result_2[key] = [0,0]
    result_2[key][0] = result_first[key][0] + total_money*0.00013
    #result_2[key][0] = result_first[key][0]
    total_money = total_money + result_2[key][0] - result_first[key][1]
    result_2[key][1] = result_first[key][1]
f2 = file('result_2.pkl','wb')
pickle.dump(result_2,f2)
f2.close()

f1 = file('tc_comp_predict_table4.csv','wb')
writer = csv.writer(f1)

for day in result_2.keys():
    dd = day + 1
    ss = "201409"
    if dd < 10:
        ss = ss + '0' + str(dd)
    else:
        ss = ss + str(dd)
    writer.writerow([ss,int(result_2[day][0]),int(result_2[day][1])])
f1.close()

