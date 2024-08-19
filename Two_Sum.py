#Given the array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 

# ex: Input: nums = [2,7,11,15]. target = 9
# output:[0,1]
# explanation: Because nums[0] + nums[1] == 9, we return [0,1]


def twoSum(nums, target):
    for i in range(len(nums)):
        if nums[i] + nums[i-1] == target:
            return [i-1, i]


if __name__ == "__main__":
    x = [2, 7, 11, 15]
    target = 9
    
    result = twoSum(x,target) 
    print(result)