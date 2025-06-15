class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Використаємо множини для пошуку перетину
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Знайдемо перетин множин
        result = list(set1 & set2)
        
        return result

# Перевірка роботи функції
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2))