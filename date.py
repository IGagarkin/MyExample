n=int(input("count of minuts: ")) 


min=n%60
hour=n//60

if hour<=23:
    clock=str(hour)+":"+str(min)
else:
    if hour%24==0:
        clock="0"+":"+str(min)
    else:
        clock=str(hour//24)+":"+str(min)
print (clock)        