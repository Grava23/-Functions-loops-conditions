#создаём переменную где будем хранить сумму всех чётных элементов
summ = 0

#создаём список где будут храниться числа последовательности фибоначи
list_of_items = [1]

#создаём список где будут храниться чётные элементы последовательности фибоначи
even_numbers = []

#создаём 2 переменные с помощью которых мы будем вычеслять последовательность фибоначи
a, b = 1, 1

#пока переменная а меньше 100000 у нас будет выполняться следующее услови:
#в каждом шаге значение b бдет прсиваеваться а, в свою очередь b будет равно сумме двух этих переменных
#переменную а мы добавляем в наш список в каждом шаге, и в конце удаляем крайний элемент списка 
# так он выходит за наше услвие
while a < 10000000:
    a, b = b, a + b
    list_of_items.append(a)
del list_of_items[-1]
print(list_of_items)


print(f"количетсво элементов в последовтельности равно: {len(list_of_items)}")

#обходим созданный списко циклом, и проверяем каждый его элемнет, делеться ли он на 2 без остатка
#если да, то суммируем его остальными чётными элементами, и добовляем в список чётных элементов
for i in list_of_items:
    if i % 2 == 0:
        summ += i
        even_numbers.append(i)
print(f"сумма всех чётных элементов ровна: {summ}")

#создаём переменную которая равна предпоследнему числу в последовательности 
number = list_of_items[-2]

 
print(f"чётные элементы списка:")
print(*even_numbers)
print(f"предпоследнее число последовательности: {number }")
