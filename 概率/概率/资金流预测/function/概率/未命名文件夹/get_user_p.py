import cPickle as pickle

def get_week_count():
    week_count = [0,0,0,0,0,0,0]
    for i in range(92):
        week_count[i%7] += 1
    return week_count

def get_purchase_p():
    week_count = get_week_count()
    usr_purchase_p = {}
    f1 = file("../data/get_678_purchase.pkl",'rb')
    usr_purchase = pickle.load(f1)
    for key in usr_purchase.keys():
        if key not in usr_purchase_p.keys():
            usr_purchase_p[key] = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for day in range(7):
            usr_purchase_p[key][day] = float(usr_purchase[key][day])/week_count[day]
    f11 = file("../data/get_purchase_p.pkl",'wb')
    pickle.dump(usr_purchase_p,f11)
    f1.close()
    f11.close()

def get_redeem_p():
    usr_redeem_p = { }
    week_count = get_week_count()
    f1 = file("../data/get_678_redeem.pkl",'rb')
    usr_redeem = pickle.load(f1)
    for key in usr_redeem.keys():
        if key not in usr_redeem_p.keys():
            usr_redeem_p[key] = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for day in range(7):
            usr_redeem_p[key][day] = float(usr_redeem[key][day])/week_count[day]
    f11 = file("../data/get_redeem_p.pkl","wb")
    pickle.dump(usr_redeem_p,f11)
    f1.close()
    f11.close()

