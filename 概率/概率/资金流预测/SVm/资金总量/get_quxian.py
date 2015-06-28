import cPickle as pickle
import matplotlib.pyplot as plt

f = file('total_purchase.txt','rb')
r1 = pickle.load(f)
r2 = pickle.load(f)
f.close()

X = []
Y1 = []
Y2 = []
for i in range(427):
    if i < 270:
        continue
    print r1[i][0]
    X.append(i)
    Y1.append(r1[i][1])
    Y2.append(r2[i][1])


plt.figure(0)
plt.plot(X,Y1)
plt.figure(1)
plt.plot(X,Y2)
plt.show()
