# encoding:utf8
import cPickle as pickle
from get_time import *
from random import random


keytime = get_time('20140101')

f1 = file("../data/概率/user_purchase_p.pkl",'rb')
f2 = file("../data/概率/user_redeem_p.pkl",'rb')
f3 = file("../data/user_平均/user_purchase_value.pkl",'rb')
f4 = file("../data/user_平均/user_redeem_value.pkl",'rb')
f5 = file("../data/关键用户/user_purchase.pkl",'rb')
f6 = file("../data/关键用户/user_redeem.pkl",'rb')

ret_purchase_p = pickle.load(f1)
ret_redeem_p = pickle.load(f2)
ret_purchase_value = pickle.load(f3)
ret_redeem_value = pickle.load(f4)
purchase_user = pickle.load(f5)
redeem_user = pickle.load(f6)

print len(ret_purchase_value)
print len(purchase_user)
print len(ret_purchase_p)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()

fromtime = get_time('20140901')
dd = (fromtime - keytime).days

result = {}

for i in range(30):
    if i not in result.keys():
        result[i] =[0,0]
    d = dd + i
    d = d % 7
    for user in purchase_user:
        if ret_purchase_p[user][d] >= random():
            result[i][0] += ret_purchase_value[user][d]
    for user in redeem_user:
        if ret_redeem_p[user][d] >= random():
            result[i][1] += ret_redeem_value[user][d]
    
  
print result

f = file('result/result.pkl','wb')
pickle.dump(result,f)
f.close()





