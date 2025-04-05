quotient =[0,0,0,0,0,0,0,0,0]#خارج قسمت 
remainder =[0,0,0,0,0,0,0,0,0]#باقی مانده
a=69 #عدد مورد نظر
remainder[0] = a % 2# یاقی مانده تقسیم بر دو
quotient[0] = a // 2# خارج قسمت تقسیم بر دو
for i in range(0,8):
    quotient[i+1] = quotient[i] // 2
    remainder[i+1] = quotient[i] % 2
print(remainder[7],remainder[6],remainder[5],remainder[4],remainder[3],remainder[2],remainder[1],remainder[0])