# -*- coding:utf-8 -*-
import cPickle as pickle
import MySQLdb
from get_time import *

class get_user_p:
    conn = ''
    cursor = ''
    def __init__(self,host = 'localhost',user = 'root',passwd = 'zhao0108',db = 'zhao'):
        self.conn = MySQLdb.connect(host,user,passwd,db)
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.conn.close()
        self.cursor.close()
    

    def get_purchase_p(self):
        ret_purchase = {}
        sql = "select * from new_balance_purchase_2014"
        #sql = "select * from balance_2014"
        ss = "  where (Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' or SubString(report_date,1,6) = '201408')"
        #ss = "  where (Substring(report_date,1,6) = '201405' or Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' )"
        sql = sql + ss
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        key_time = get_time('20140101')
        #week_count = [35,35,35,35,35,34,34]
        week_count = [14,13,13,13,13,13,13]
        #week_count = [18,18,18,18,17,17,17]
        i = 0
        for row in rows:
            i = i + 1
            if i % 10000 == 0:
                print i
            id,user_id,report_date,tBalance,yBalance,total_purchase_amt,direct_purchase_amt,purchase_bal_amt,purchase_bank_amt,total_redeem_amt,consume_amt,transfer_amt,tftobal_amt,tftocard_amt,share_amt,category1,category2,category3,category4 = row
            if user_id not in ret_purchase.keys():
                ret_purchase[user_id] = {0:0,1:0,2:0,3:0,4:0,5:0,6:0 }
            day = (get_time(report_date) - key_time).days
            day = day%7
            ret_purchase[user_id][day] += 1
        for user in ret_purchase.keys():
            for day in range(7):
                ret_purchase[user][day] = float(ret_purchase[user][day])/week_count[day]
        f = file("../../data/概率/user_purchase_p.pkl",'wb')
        pickle.dump(ret_purchase,f)
        f.close()




    def get_redeem_p(self):
        ret_redeem = {}
        sql = "select * from new_balance_redeem_2014"
        #sql = "select * from balance_2014"
        ss = "  where (Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' or SubString(report_date,1,6) = '201408')"
        #ss = "  where (Substring(report_date,1,6) = '201405' or Substring(report_date,1,6) = '201406' or SubString(report_date,1,6) = '201407' )"
        sql = sql + ss
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        key_time = get_time('20140101')
        #week_count = [35,35,35,35,35,34,34]
        week_count = [14,13,13,13,13,13,13]
        #week_count = [18,18,18,18,17,17,17]
        i = 0
        for row in rows:
            i = i + 1
            if i % 10000 == 0:
                print i
            id,user_id,report_date,tBalance,yBalance,total_purchase_amt,direct_purchase_amt,purchase_bal_amt,purchase_bank_amt,total_redeem_amt,consume_amt,transfer_amt,tftobal_amt,tftocard_amt,share_amt,category1,category2,category3,category4 = row
            if user_id not in ret_redeem.keys():
                ret_redeem[user_id] = {0:1,1:0,2:0,3:0,4:0,5:0,6:0 }
            day = (get_time(report_date) - key_time).days
            day = day%7
            ret_redeem[user_id][day] += 1
        for user in ret_redeem.keys():
            for day in range(7):
                ret_redeem[user][day] = float(ret_redeem[user][day])/week_count[day]
        f = file("../../data/概率/user_redeem_p.pkl",'wb')
        pickle.dump(ret_redeem,f)
        f.close()






