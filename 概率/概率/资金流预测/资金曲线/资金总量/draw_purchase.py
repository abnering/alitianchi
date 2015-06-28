import cPickle as pickle
import matplotlib.pyplot as plt



f= file('total_purchase.txt','rb')
total_purchase = pickle.load(f)
total_redeem = pickle.load(f)
f.close()
'''
for item in total_purchase:
    if item[1] > 350000000:
        print item
'''

for item in total_purchase:
    if item[0] > '20140731':
        print item

X = []
Y = []
i = 0
for item in total_purchase:
    if item[0] > '20140431' and item[0] < '20140701': 
        i += 1
        X.append(i)
        Y.append(item[1])
plt.figure(1)
plt.plot(X,Y)
plt.show()
