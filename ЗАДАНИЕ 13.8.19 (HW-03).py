tickets=int(input("Какое количество билетов на конференцию Вам необходимо? "))
ages = [int(input("Возраст участника конференции - ")) for i in range(tickets)]

S = 0
a = 0
while a < len(ages):
  print("Возраст участника конференции", ages[a], "лет")
  if ages[a] < 18:
        price = 0
        print("Участие в конференции бесплатно")
        a += 1
  elif  18 <= ages[a] < 25:
    price = 990
    print("Стоимость билета ", price, "рублей")
    S += price
    a += 1
  elif ages[a]>=25:
      price = 1390
      print("Стоимость билета ", price, "рублей")
      S += price
      a += 1
if tickets>=3:
    S = S*0.9
    print ("Стоимость всех билетов со скидкой 10% = ",S, "рублей")
else:
    print("Стоимость всех билетов =",S, "рублей")
