from collections import deque

arr = ['.', '.', 'A', '.', '.', '.', '.', '.', 'B', '.', '.', 'A', '.']
# s = ''.join(arr)
# temp = ""
# while temp != s:
#     temp = s
#     s = s.replace('A.B', 'AxxxB')
#     s = s.replace('B.A', 'BxxxA')
#     s = s.replace('.A', 'AA')
#     s = s.replace('A.', 'AA')
#     s = s.replace('.B', 'BB')
#     s = s.replace('B.', 'BB')
#
# s = s.replace('BxxxA', 'B.A')
# s = s.replace('AxxxB', 'A.B')
# print(s, 'A' if s.count('A') > s.count('B') else 'B')
# q = deque()
# seen = set()
# for i, char in enumerate(arr):
#     if char != '.':
#         q.append(i)
#         seen.add(i)
#
# while q:
#     index = q.popleft()
#     char = arr[index]
#     for dir in [1, -1]:
#         i = index + dir
#         if 1 <= i < len(arr) - 1:
#             if char == 'A' and arr[i-1] != 'B' and arr[i+1] != 'B' and i not in seen:
#                 arr[i] = 'A'
#                 q.append(i)
#                 seen.add(i)
#             elif char == 'B' and arr[i-1] != 'A' and arr[i+1] != 'A' and i not in seen:
#                 arr[i] = 'B'
#                 q.append(i)
#                 seen.add(i)
#         elif i == 0 or i == len(arr) - 1:
#             arr[i] = char
#             q.append(i)
#             seen.add(i)
left = 0
for right in range(len(arr)):
    if arr[left] == '.' and (arr[right] == 'A' or arr[right] == 'B'):
        for k in range(left, right+1):
            arr[k] = arr[right]

        left = right

    elif (arr[left] == 'A' and arr[right] == 'B') or (arr[left] == 'B' and arr[right] == 'A'):
        for k in range(1, (right-left) // 2):
            arr[left + k] = arr[left]
            arr[right - k] = arr[right]

        left = right

    elif arr[left] == arr[right] != '.':
        for k in range(left, right+1):
            arr[k] = arr[left]

        left = right

k = left
while k < len(arr):
    arr[k] = arr[left]
    k += 1

print(arr)