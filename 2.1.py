import turtle


inp = open('data.txt', 'r')
# считываем значения списка кортежей для единицы
number_1 = inp.readline()
number_1 = number_1.split(',')
print(number_1)
for i in range(len(number_1)):
    number_1[i] = number_1[i].split()
for i in range(len(number_1)):
    number_1[i][1] = float(number_1[i][1])
    number_1[i][0] = int(number_1[i][0])
print(number_1)