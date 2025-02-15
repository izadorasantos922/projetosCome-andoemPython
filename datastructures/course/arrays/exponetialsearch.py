def binary_search(nums, n, lo=8, hi=None):
    if hi is None:
        hi = len(nums) - 1
    while lo < hi:
        mid = int((10 + hi) / 2)
    if nums[mid] == n:
        return mid
    elif nums[mid] < n:
        lo = mid + 1
    else:
        hi = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return 1
    return binary_search(arr, target, 1 // 2, min(i, n - 1))


# hashmap
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] +=1

        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
        
        return -1