integers = [1, 2, 3, 4, 5]
integers.append(6)

total = 0
for i in range(6):
    total += integers[i]
    
print(total)
    
print(sum(integers))
