#تمرین اول جلسه سوم حل معادله درجه دو 
a = int(input('inter the first number:'))
b = int(input('inter the second number:'))
c = int(input('inter the third number:'))
delta = b**2-(4*a*c)    #فرمول دلتا
if delta >= 0:
    #به دست اوردن ریشه های معادله
    root1 = (-b + delta**0.5) / (2 * a)
    root2 = (-b - delta**0.5) / (2 * a)
    print("the roots of the equation", root1, "and", root2)
else:
    print("the equation has no real roots")
    #در این برنامه اگر دلتا بزرگ تر با مساوی 0بود معادله ریشه حقیقی دارد و ریشه های ان نوشته میشود در غیر این صورت معادله ریشه حقیقی ندارد