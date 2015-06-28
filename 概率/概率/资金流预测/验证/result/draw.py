import cPickle as pickle
import matplotlib.pyplot as plt

f = file('result.pkl','rb')
ret = pickle.load(f)
f.close()

X = []
Y1 = []
Y2 = []

for key in ret.keys():
    X.append(key)
    Y1.append(ret[key][0])
    Y2.append(ret[key][1])
plt.figure(1)
plt.plot(Y1,'c-')
plt.figure(2)
plt.plot(Y2,'m-')
plt.show()
