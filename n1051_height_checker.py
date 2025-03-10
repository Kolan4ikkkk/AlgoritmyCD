class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        mismatch = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch += 1
        return mismatch