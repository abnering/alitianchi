# -*- coding:utf-8 -*-
import cPickle as pickle
import MySQLdb
from get_time import *

class get_user_mean:
    conn = ''
    cursor = ''
    def __init__(self,host = 'localhost',user = 'root',passwd = 'zhao0108',db = 'zhao'):
        self.conn = MySQLdb.connect(host,user,passwd,db)
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.conn.close()
        self.cursor.close()
    

    def get_purchase_day(self):
        ret_purchase = {}
        sql = "select * from  new_balance_purchase_2014"
        ss = "  where (Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' or SubString(report_date,1,6) = '201408')"
        #ss = "  where (Substring(report_date,1,6) = '201405' or Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407')"
        sql = sql + ss
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        key_time = get_time('20140101')
        i = 0
        for row in rows:
            i = i + 1
            if i % 10000 == 0:
                print i
            id,user_id,report_date,tBalance,yBalance,total_purchase_amt,direct_purchase_amt,purchase_bal_amt,purchase_bank_amt,total_redeem_amt,consume_amt,transfer_amt,tftobal_amt,tftocard_amt,share_amt,category1,category2,category3,category4 = row

            day = (get_time(report_date) - key_time).days
            if day not in ret_purchase.keys():
                ret_purchase[day] = 0
            #day = day%7
            ret_purchase[day] += 1       
        f = file("data/user_purchase_day.pkl",'wb')
        pickle.dump(ret_purchase,f)
        f.close()




    def get_redeem_day(self):
        ret_redeem = {}
        sql = "select * from new_balance_redeem_2014"
        ss = "  where ( Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' or SubString(report_date,1,6) = '201408')"
        #ss = "  where (Substring(report_date,1,6) = '201405' or Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407')"
        sql = sql + ss
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        key_time = get_time('20140101')       
        i = 0
        for row in rows:
            i = i + 1
            if i % 10000 == 0:
                print i
            id,user_id,report_date,tBalance,yBalance,total_purchase_amt,direct_purchase_amt,purchase_bal_amt,purchase_bank_amt,total_redeem_amt,consume_amt,transfer_amt,tftobal_amt,tftocard_amt,share_amt,category1,category2,category3,category4 = row

            day = (get_time(report_date) - key_time).days
            #day = day%7
            if day not in ret_redeem.keys():
                ret_redeem[day] = 0
            ret_redeem[day] += 1        
        f = file("data/user_redeem_day.pkl",'wb')
        pickle.dump(ret_redeem,f)
        f.close()






