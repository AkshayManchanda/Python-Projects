import time
import datetime
birth_date = input('Enter the date(YYYY-MM-DD):')
print('\n')
pattern ='%Y-%m-%d'
epoch1 = int(time.mktime(time.strptime(birth_date, pattern)))
print ('Given date epoch: ', epoch1)

todays_date=datetime.datetime.now().date()
print('Today\'s Date:', todays_date)
epoch2 = int(time.mktime(time.strptime(str(datetime.datetime.now().date()), pattern)))
print ('Current date epoch: ', epoch2)

epoch=epoch2 - epoch1

print('\n')
print('You are....')
print('Seconds: ', epoch)
print('Or')
print('Minutes: ', (epoch)/60)
print('Or')
print('Hours:', (epoch)/3600)
print('Or')
print('Days: ',(epoch)/86400)
print('Or')
print('weeks: ',epoch//(86400*7),end='  ')
print('days:',int((epoch%(86400*7))/86400))
a=time.strptime(str(todays_date),pattern)
b=time.strptime(str(birth_date),pattern)
years=a.tm_year-b.tm_year
months=a.tm_mon-b.tm_mon
days=a.tm_mday-b.tm_mday
if days<0:
    months=months-1
    days=days+30
if months<0:
    years=years-1
    months=months+12
print('or\nmonths: ',years*12+months,end=' ')
print('days: ',days)
print('or')
print('Years: ',years,end=' ')
print('Months: ' ,months, end=' ')
print('Days: ',days, end=' ')