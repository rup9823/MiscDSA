nums = [12, 34, 67, 90]
k = 2


def partition(i, k):
    if k == 1:
        return sum(nums[i:])

    if i == len(nums):
        return float("inf")

    current_sum = 0
    ans = float("inf")
    for j in range(i, len(nums)):
        current_sum += nums[j]
        partition_sum = partition(j+1, k-1)
        temp_sum = max(current_sum, partition_sum)
        ans = min(ans, temp_sum)

    return ans


print(partition(0, k))
