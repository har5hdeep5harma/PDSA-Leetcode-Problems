class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        for k in range(n // 2 + 1):
            ans += self.factorial(n - k) // (
                self.factorial(k) *
                self.factorial(n - 2 * k)
            )

        return ans

    def factorial(self, m):
        if m == 0 or m == 1:
            return 1
        return m * self.factorial(m - 1)