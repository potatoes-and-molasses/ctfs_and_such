import datetime

years=filter(lambda x: x.weekday()==3,[datetime.date(int('1%02d6' % i),1,1) 
                                 for i in range(100)])

for i in years:
	try:
		datetime.date(i.year,2,29)
		print i
	except:
		None
#apparently mozart's birth date(second youngest of possible years)
