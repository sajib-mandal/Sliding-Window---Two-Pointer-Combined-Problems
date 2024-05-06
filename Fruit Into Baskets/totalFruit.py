class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left, right, maxLen = 0, 0, 0
        mpp = {}
        while right < n:
            mpp[fruits[right]] = mpp.get(fruits[right], 0) + 1
            if len(mpp) > 2:
                mpp[fruits[left]] -= 1
                if mpp[fruits[left]] == 0:
                    del mpp[fruits[left]]
                left += 1
            if len(mpp) <= 2:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
        
