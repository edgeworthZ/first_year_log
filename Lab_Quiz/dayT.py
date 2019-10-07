def isLeapYear(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def day(y=2016,m=2,d=1):
  diff1,diff2 = 0,0
  month = [31,28,31,30,31,30,31,31,30,31,30,31]
  days = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednasday', 'Thursday']
  mm = ['','January','February','March','April','May','June','July','August','September','October','November','December']
  for i in range(1970, 2016):
    if isLeapYear(i):
      diff1 = diff1 + 366
    else:
      diff1 = diff1 + 365
  diff1 = diff1 + 1 # add 1 Jan 2016
  for i in range(1970, y):
    if isLeapYear(i):
      diff2 = diff2 + 366
    else:
      diff2 = diff2 + 365
  for i in range(m-1):
    diff2 = diff2 + month[i]
    if i==2 and isLeapYear(y):
      diff2 = diff2 + 1
  for i in range(d):
    diff2 = diff2 + 1
  diff = abs(diff1 - diff2)%7
  if diff2 < diff1:
    diff = 7 - diff
  print(f'diff1={diff1}, diff2={diff2}, diff={diff}')
  print(f'{d} {mm[m]} {y} is {days[diff]}.')

day(1246,2,28)
