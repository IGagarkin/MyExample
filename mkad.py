V=105

T=150
S=0

while T>0:
    S=(S+V)%109
    # if V<0:
        # S=109-S 
    T-=1
    print (S)

print (S)    