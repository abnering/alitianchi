import datetime

def get_time(date_str):
    t1 = int(date_str[0:4])
    t2 = int(date_str[4:6])
    t3 = int(date_str[6:8])
    return datetime.datetime(t1,t2,t3)
