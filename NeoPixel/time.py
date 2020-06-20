import datetime

a=  (datetime.datetime.now()+ datetime.timedelta(minutes=5))
print (a.time())
    

while (1==1):
    rn = str(datetime.datetime.now().time())
    a=  (datetime.datetime.now()+ datetime.timedelta(minutes=5))
    if rn >= str(a.time()) and rn <= str(a.time()) :
        print ("ya!!")
    if rn >= "23:57:04.000000" and rn <= "23:57:04.000100" :
        print ("ya! pues!")


