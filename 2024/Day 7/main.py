with open("input.txt") as f:
    lines = f.read().split("\n")
    data = {}
    for line in lines:
        value, nums = line.split(": ")
        value = int(value)
        nums = [int(x) for x in nums.split(" ")]
        data[value] = nums
    
def is_possible(value, nums, part=1):
    n = len(nums)
    operators = ["+", "*", "||"]
    results = [nums[0]]
    for i in range(1, n):
        new_results = []
        for result in results:
            if result > value: continue
            for op in operators:
                if op == "+": new_results.append(result + nums[i])
                if op == "*": new_results.append(result * nums[i]) 
                if part == 2 and op == "||":
                    new_results.append(int(str(result) + str(nums[i])))
        results = new_results
    
    return any(result == value for result in results)

total, total2 = 0, 0
for value, nums in data.items():
    if is_possible(value, nums): 
        total += value
        total2 += value
    elif is_possible(value, nums, part=2): total2 += value
    
print(f"Part 1: {total}")
print(f"Part 2: {total2}")