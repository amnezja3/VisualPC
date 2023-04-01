
flags = {'s2:#':'a', 's5:#':'b', 's7:#':'c', 's9:#':'d'}
sequence = {'s1:#':'xx', 's2:#':'xx', 's3:#':'xx', 's4:#':'xx', 's5:#':'xx', 's6:#':'xx', 's7:#':'xx', 's8:#':'xx', 's9:#':'xx'}

l1 = ['piernik', 'makowiec', 'sernik']
l2 = ['mlotek', 'kombinerki', 'srubowkret']
l3 = ['siano', 'karma', 'zwirek']
l4 = ['zwir', 'piasek', 'kruszywo']

def signer(seq, flag):
    # oznacznie flag w pojedyńczej sekwencji zwraca słownik z podmienionymi wartosciami wedlug klucza
    for l in flag.keys():
        for s in seq.keys():
            if s == l:
                seq[s]=flag[s]
    return seq

def replacer(dict, a,b,c,d):
    # podmiana flag dla wybranego ID
    w = []
    for k, v in dict.items():
        if v=='a':        
            dict[k]=l1[a]
        if v=='b':        
            dict[k]=l2[b]
        if v=='c':        
            dict[k]=l3[c]
        if v=='d':        
            dict[k]=l4[d]  
    for ll in dict.values():
        w.append(ll)    
    return w

def loop(seq,fla, aa,bb,cc,dd):
    ia = int(len(aa))
    ib = int(len(bb))
    ic = int(len(cc))
    id = int(len(dd))
    for a in range(ia):
        for b in range(ib):
            for c in range(ic):
                for d in range(id):
                    r = signer(seq, fla)
                    w = replacer(r, a,b,c,d, aa,bb,cc,dd)
                    print(w)


print(loop(sequence, flags, l1,l2,l3,l4))
