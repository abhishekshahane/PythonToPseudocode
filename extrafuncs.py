def check(f):
    while('' in f) : 
        f.remove('')
    return f 
def alphnum(f):
    stra=""
    c = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    for i in range(len(f)):
        if f[i] not in c and f[i] not in ' ':
            stra+=f[i]
    return stra



