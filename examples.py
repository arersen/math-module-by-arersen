import mathbyarersen as math #сокращения используем чисто для удобного использования
while True:
  type = input("Выберите которую вы функцию хотите использовать:\nlog\nsqrt\nfact\n")
  if type == "fact":
    a = int(input("Введите число: "))
    res = math.fact(a)
    print(res)
  if type == "log":
    a = int(input("Введите по какому основанию будет логарифм "))
    b = int(input("Введите число: "))
    c = math.log(a,b)
    print(c)
  if type == 'rtod':
        a = input('Введите число')
            print(math.RandD.RtoD(a))
  if type == 'dtor':
        a = input('Введите число')
        print(math.RandD.RtoD(a))
  if type == "sqrt":
    num = int(input("Введите число: "))
    if num < 0:
      print("ОШИБКА:Корня квадратного из отрицательного числа быть не может.")
    elif num >= 0:
      res = math.sqrt(num)
      print(res)
   
 
      
      
      
  
