1)lower triangle pattern

n = int(input("Enter the number of rows: "))
# print lower triangle pattern
for i in range(1, n + 1):
    print('* ' * i)

2)upper triangle pattern

n = int(input("Enter the number of rows: "))
# print upper triangular pattern
for i in range(n, 0, -1):
    print('* ' * i)


3) pyramid pattern


n = int(input("Enter the number of rows: "))
# print pyramid pattern
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('* ' * i)

