
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(map(float, per_cent.values()))
print(per_cent_list)
money = int(input('Какую сумму вы планируете вложить?'))
deposit = [i * money/100 for i in per_cent_list]
deposit_int = list(map(int,deposit))
deposit_int.sort(reverse=True)
print('Максимальная сумма, которую вы можете заработать - ', deposit_int[0], 'р')