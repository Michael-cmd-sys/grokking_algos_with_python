def find_max(nums:list[int]) -> int:
    max = 0
    if nums is None:
        return None
    
    max = nums[0]
    for num in nums[1:]:
        if num > max:
            max = num
            
    return max

test_1 = [1e-3, 3, 0, 43, 232, 65, 905]
print(find_max(test_1))
