def heightChecker(heights):
    expected = sorted(heights)
    mismatch = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            mismatch += 1
    return mismatch

print(heightChecker([1, 1, 4, 2, 1, 3]))  
print(heightChecker([5, 1, 2, 3, 4]))     
print(heightChecker([1, 2, 3, 4, 5]))     