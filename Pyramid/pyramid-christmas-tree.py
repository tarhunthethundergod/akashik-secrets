#!/usr/bin/python3

n = int(input('How many layers?: '))

def pyramid(n, padding = 0):
  for i in range(1, n + 1):
    print(('^ ' * i).rjust(padding + n + i))

for i in range(1, n + 1):
  pyramid(i, n - i)
