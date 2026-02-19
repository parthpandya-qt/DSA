def duplicate(nums):
    slow=nums[0]
    fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    slow=0
    while True:
        slow=nums[slow]
        fast=nums[fast]
        if slow==fast:
            return slow