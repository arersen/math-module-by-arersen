#import mathbyarersen as math
#используйте ключевое слово ''as'' для сокращения импорта
#print(math.sqrt(число,либо переменная)
def sqrt(b):
	a = b ** (1/2)
	return a
#///////////////////////////////////////////////
#Пример использования:
#import mathbyarersen as math
#a = math.log(основа,число)
#print(a)
def log(x,y):
  return ln(y)/ln(x)
def ln(x):
  return x/1-x**2/2+x**3/3-x**4/4+x**5/5-x**6/6+x**7/7
#он почти точно считает, считал бы точно,если бы я был не говнопитонистом
#//////////////////////////////////////////////
#округлитель числа
#пример использования:
#math.rtn(параметр,1 округливать до целого числа. 0.1 до одной десятой. либо 0.01)
"""def rtn(c,f):
	if f = 0.1:
		c
		#не доработано!!!!!!!
"""
#по умолчанию ставим 0
#print(math.PI.pi(0))
class PI:
	def pi(a):
		num = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337
		return (num + a)
	#math.SQRT.sqrt(число,степень)
class SQRT:
	def sqrt(a,b):
		num = a
		step = 1 / b
		res = a ** (1 / b)
		return res
	#факториалы
def fact(n):
	pr = 1
	for i in range(1 , n + 1):
		pr  = pr * i;
	return pr
class DtoR:
	def RtoD(value):
		pi = PI.pi(0)
		res = value * (pi / 180)
		return res
	def DtoR(value):
		pi = PI.pi(0)
		res = value * (180 / pi)
		return res
		
	
