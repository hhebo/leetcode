# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
  return -1 if nums.length < 3
  result = 0
  distance = 1_073_741_823
  nums.sort!
  (0...nums.length - 2).each do |i|
    j = i + 1
    k = nums.length - 1
    while j < k
      temp = nums[i] + nums[j] + nums[k]
      if temp < target
        temp_dist = target - temp
        if temp_dist < distance
          result = nums[i] + nums[j] + nums[k]
          distance = temp_dist
        end
        j += 1
      elsif temp > target
        temp_dist = temp - target
        if temp_dist < distance
          result = nums[i] + nums[j] + nums[k]
          distance = temp_dist
        end
        k -= 1
      else
        return nums[i] + nums[j] + nums[k]
      end
    end
  end
  result
end
