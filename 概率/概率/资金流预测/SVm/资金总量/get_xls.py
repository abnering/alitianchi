#encoding:utf8
import xlwt
import numpy as np
import cPickle as pickle

f = file('total_purchase.txt','rb')
r1 = pickle.load(f)
r2 = pickle.load(f)
f.close()

workbook = xlwt.Workbook(encoding = 'utf-8')
booksheet = workbook.add_sheet('Sheet1',cell_overwrite_ok = True)

l = len(r1)
for i in range(l):
    booksheet.write(i,0,r1[i][1])
    booksheet.write(i,1,r2[i][1])
    i += 1
workbook.save('data.xls')

