#encoding:utf8
import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt


f = file('资金总量/total_purchase.txt','rb')
day_purchase = pickle.load(f)
day_redeem = pickle.load(f)
f.close()
f1 = file('result.pkl','rb')
result = pickle.load(f1)
f1.close()
X = []
Y1 = []
Y2 = []
i = 0

for item in day_purchase:
    i += 1
    X.append(i)
    print item[0]
    Y1.append(item[1])

for item in result.keys():
    i += 1
    X.append(i)
    Y1.append(result[item][0])
print i
for item in day_redeem:
    Y2.append(item[1])

for item in result.keys():
    Y2.append(result[item][1])

plt.figure(1)
plt.plot(X,Y1,'r')
plt.figure(2)
plt.plot(X,Y2,'r')
plt.show()
