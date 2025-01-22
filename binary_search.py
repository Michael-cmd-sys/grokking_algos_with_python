def bin_search(nums: list[int], target: int) -> int:
    if nums is None:
        return -1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
            
    return -1
print(bin_search([1, 34, 54, 765, 788, 895, 1001, 1010, 1100, 1101, 1110, 1111, 2343, 3454, 5644, 7545], 5644))