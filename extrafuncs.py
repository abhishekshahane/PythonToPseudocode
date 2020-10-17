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
class String:
    def __init__(self, give):
        self.give = give
    def alphanum(self):
        stra=""
        c = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        for i in range(len(self.give)):
            if self.give[i] not in c and self.give[i] not in ' ':
                stra+=self.give[i]
        return stra