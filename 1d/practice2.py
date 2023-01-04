# Pairs/ Two Sum
li = [1,2,4,6,11,9,17,5,1]

def pairnum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                print(nums[i],nums[j])
#pairnum(li,6)

# Pair Product  max number
def maxproduct(list):
    max_product = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] * list[j] > max_product:
                max_product = list[i] * list[j]
                pair = str(list[i]) + " " + str(list[j])
    return max_product,pair
print(maxproduct(li))

# is unique
def isunique(list):
    list2 = []
    for i in list:
        if i in list2:
            return False
        else:
            list2.append(i)
    return True

print(isunique(li))

