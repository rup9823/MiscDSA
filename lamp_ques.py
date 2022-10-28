import heapq
from sortedcontainers import SortedDict

lamps = [[1, 7], [5, 11], [7, 9]]
points = [7, 1, 5, 10, 9, 15]

# offPoints = list(zip(points, [i for i in range(len(points))]))
# offPoints.sort()
#
# lamps.sort()
#
# minH = []
# index = 0
# ans = [0] * len(points)
#
# for i in range(len(points)):
#     while index < len(lamps) and lamps[index][1] >= offPoints[i][0] >= lamps[index][0]:
#         heapq.heappush(minH, lamps[index][1])
#         index += 1
#
#     while minH and minH[0] < offPoints[i][0]:
#         heapq.heappop(minH)
#
#     ans[offPoints[i][1]] = len(minH)

dict = SortedDict()
for s, e in lamps:
    dict[s] = dict.get(s, 0) + 1
    dict[e+1] = dict.get(e+1, 0) - 1

ans = []

for l in points:
    cur = 0
    for key, val in dict.items():
        if key > l:
            break
        cur += val
    ans.append(cur)

print(ans)