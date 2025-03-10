class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Створюємо словник для зберігання порядку елементів з arr2
        order = {num: i for i, num in enumerate(arr2)}
        
        # Функція для сортування
        def custom_sort(x):
            return order.get(x, len(arr2) + x)
        
        # Сортуємо arr1 з використанням нашої функції сортування
        arr1.sort(key=custom_sort)
        return arr1