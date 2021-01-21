summ = 0
for i in range(1000,20000):
    if i % 3 == 0 and i % 5 == 0:
        summ += i 
print(f"сумма равна: {summ}")