# -*-encoding:utf8-*-
import cPickle as pickle

def get_purchase_user():
    f = file('../../data/关键用户/user_purchase.pkl','wb')
    
    f1 = file('../../data/概率/user_purchase_p.pkl','rb')
    ret_purchase = pickle.load(f1)
    purchase_user = set()
    for user in ret_purchase.keys():
        purchase_user.add(user)
    f1.close()
    pickle.dump(purchase_user,f)
    f.close()

def get_redeem_user():
    f = file('../../data/关键用户/user_redeem.pkl','wb')
    f1 = file('../../data/概率/user_redeem_p.pkl','rb')
    ret_redeem = pickle.load(f1)
    redeem_user = set()
    for user in ret_redeem.keys():
        redeem_user.add(user)
    pickle.dump(redeem_user,f)
    f1.close()
    f.close()



