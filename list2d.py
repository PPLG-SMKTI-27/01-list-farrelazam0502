nilai = [[10,20,30],
         [40,50,60],
         [70,80,90]]

for i in range (len(nilai)):
    for j in range (len(nilai[i])):
        print (nilai [i] [j], end="")
    print()    

nilai = [[10,20,30],
         [40,50,60],
         [70,80,90]]

for i in nilai:
    sum = 0
    for j in i :
        sum+=j
    print(sum)    