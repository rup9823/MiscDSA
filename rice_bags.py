'''
You are given an array riceBags which stores the number of rice grains in every rice bag. A "perfect collection" is
defined as a subset of riceBags such that perfect_collection[i+1] == perfect_collection[i]*perfect_collection[i].
Return the max size of perfect collection that's possible. Note: No duplicates in riceBags.
If the max size is < 2, you should return -1

Ex1: riceBags = [3, 9, 4, 2, 16] Possible perfect collections are - [3, 9], [2, 4], [4, 16], [2, 4, 16].
You should return 3 as [2, 4, 16] is the largest perfect collection

Ex2: riceBags = [7, 4, 8, 9] should return -1 as there is no perfect collection

Ex3: riceBags = [625, 4, 2, 5, 25]
possible perfect collections are [25, 625], [2, 4], [5, 25], [5, 25, 625], should return 3
'''
import math

rice_bags = [[3, 9, 4, 2, 16], [7, 4, 8, 9], [625, 4, 2, 5, 25, 390625]]
for rice_bag in rice_bags:
    rice_set = set(rice_bag)
    longest = 0
    for rice in rice_bag:
        if rice ** 2 not in rice_set:
            r = math.sqrt(rice)
            streak = 1
            while r in rice_set:
                streak += 1
                r = math.sqrt(r)
            longest = max(longest, streak)
    longest = -1 if longest < 2 else longest
    print(longest)

