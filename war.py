import datetime
now = datetime.datetime.now()
a = now.strftime("%Y-%m-%d")
b = "2022-02-24"
a = a.split('-')
b = b.split('-')
aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
bb = datetime.date(int(b[0]),int(b[1]),int(b[2])-1)
cc = aa-bb
dd = str(cc)
print('Война началась:',dd.split()[0], 'дней назад') 

