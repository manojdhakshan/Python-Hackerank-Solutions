from calendar import weekday,day_name
a = (input())
b=a.split()
c=(weekday(int(b[2]),int(b[0]),int(b[1])))
dayName = day_name[c]
print(dayName.upper())
