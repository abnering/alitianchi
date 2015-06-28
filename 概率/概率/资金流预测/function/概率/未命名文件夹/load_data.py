import cPickle as pickle

def get_purchase_p():
    f = file('../data/get_purchase_p.pkl','rb')
    return pickle.load(f)

def get_redeem_p():
    f = file('../data/get_redeem_p.pkl','rb')
    return pickle.load(f)
