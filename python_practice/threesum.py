"""The idea is to first sort nums, and iterate over all possible values nums[i] for the smallest number in the
triple. For each value, we need to find a pair nums[j], nums[k] with i < j < k such that nums[j] + nums[k] == -nums[
i]"""


def myfunction(nums):
    res = []
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        new_target = -nums[i]
        while j < k:
            summ = nums[j] + nums[k]
            if summ < new_target:
                j += 1
            elif summ > new_target:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j + 1] == nums[j]:
                    j += 1
                j += 1
                while k > j and nums[k - 1] == nums[k]:
                    k -= 1
                k -= 1
    return res


lst = list(map(int, input().split(",")))
print(myfunction(lst))

# time complexity: O(n**2)
# space complexity: O(1)
