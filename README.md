# 12.7.3 (HW-03)

rate = list(per_cent.values())
money = int(input("Сумма для депозита: "))
year_depositТКБ = (rate[0]*money/100)
year_depositСКБ = (rate[1]*money/100)
year_depositВТБ = (rate[2]*money/100)
year_depositСБЕР = (rate[3]*money/100)
deposit =[year_depositТКБ, year_depositСКБ, year_depositВТБ, year_depositСБЕР]
print(deposit)


a= {'доходность ТКБ': rate[0]*money/100, 'доходность СКБ' : rate[1]*money/100, 'доходность ВТБ' : rate[2]*money/100, 'доходность СБЕР' : rate[3]*money/100  }
print(a)
deposit_i=(max(deposit))
print("Максимальный возможный доход -  ", deposit_i)
