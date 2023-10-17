def twoSum(nums, target):
    # Create a hash map to store the complement of each number
    complement_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the map
        if complement in complement_map:
            return [complement_map[complement], i]
        
        # If the complement doesn't exist, add the current number to the map
        complement_map[num] = i
    
    # If no solution is found, return an empty list
    return []