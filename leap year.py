year=int(input('Enter your desired year:'))  #وارد کردن سال مورد نظر توسط کاربر
if(year % 4 ==0 and year % 100 !=0) or (year % 400 ==0): # بررسی سال که بر 4و400 بخش پذیر و به 100 نیاشد
    print('The' '{year} is a leap year.') # سال کبیسه است
else:
    print('The' '{year} is not a leap year.') # سال کبیسه نیست