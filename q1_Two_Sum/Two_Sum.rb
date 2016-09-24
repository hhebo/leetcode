# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  result = []
  hash = {}
  hash[nums[0]] = 0
  (1...nums.length).each do |i|
      temp = target - nums[i]
      if hash.has_key?(temp)
          result << hash[temp]
          result << i
          return result
      else
          hash[nums[i]] = i
      end
  end
  result
end
