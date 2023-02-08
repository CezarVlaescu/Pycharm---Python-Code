# array form = [x1, x2, x3........y1, y2, y3]
# the array lenght is 2n, n is giving by user
# returned array = [ x1, y1, x2, y2 ....... ]

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = [0] * (2 * n)
        for i in range(n):
           ans[2 * i] = nums[i]
           ans[2 * i + 1] = nums[i + n]
        return ans

print(Solution.shuffle())