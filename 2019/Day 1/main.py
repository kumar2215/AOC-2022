with open('input.txt') as f:
    nums = [int(num) for num in f.read().split('\n')]
    nums1 = [num // 3 - 2 for num in nums]

def get_total_fuel(num):
    next_n = num // 3 - 2
    return 0 if next_n <= 0 else next_n + get_total_fuel(next_n)

nums2 = [get_total_fuel(num) for num in nums]

print(f"Part 1: {sum(nums1)}")
print(f"Part 2: {sum(nums2)}")
