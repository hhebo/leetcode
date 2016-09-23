# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    result = []
    hash = {}
    hash.store(nums[0], 0)
    for i in 1...nums.length
        temp = target - nums[i]
        if hash.has_key?(temp)
            result << hash[temp]
            result << i
            return result
        else
            hash.store(nums[i], i)
        end
    end
    result
end
