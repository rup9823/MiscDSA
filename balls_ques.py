'''
n no of balls is given. They are arranged in a triangle
    *
   * *
  * * *
  for n = 6
Find number of complete rows.
'''
n = 7
curr = 0
i = 0
while curr <= n:
    i += 1
    curr += i

print(i - 1 if curr > n else i)