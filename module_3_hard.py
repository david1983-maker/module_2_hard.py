num = int(input(' Enter number from 3 , until 20: '))

for i in range(1, num):
    for j in range(i + 1, num):
        if num % (i + j) == 0:

          print(i,j, end=' ')
