from typing import Callable

def get_selection_sort_details(func: Callable[[list[int]], list[int]]) -> str:
    def wrapper(args: list[int]) -> str:
        result = func(args)
        if result:
            return f"Sorted list is {result}"

    return wrapper

@get_selection_sort_details
def selection_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    if nums is None:
        return None
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
                nums[i], nums[min_idx] = nums[min_idx], nums[i] 

    return nums

list_1 = [23, 1, 6, 7868, 2, 35, 232, 546, 766, 9, 30]
list_2 = [-34, 54, 3, -4, 23, -43, 343, 344, 12]

print(selection_sort(list_1))
print(selection_sort(list_2))
